#!/usr/bin/python3
# -*- coding: utf-8 -*-

# LN 2018-07-11
# Couldn't get the delete to work with REST (but with the Python API), so I decided to use the Python API instead. 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# CONSTANTS
ORDINAL = 'ordinal'
TODO = 'todo'

def initialize_database_connection():
    # Retrieve credentials.
    cred = credentials.Certificate('./fiftyone-a1bf4-firebase-adminsdk-plp8l-d4e881d092.json')
    
    # Initialize the API so that it points to the database we want to use. Supply the credentials we just read.
    firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://fiftyone-a1bf4.firebaseio.com'
    })

def get_reference_to_todos_collection():
    # Get a ref to the notes collection.
    todos = db.reference('todos')
    return todos

def delete_todo_from_database(ordinal):
    # Get a ref to the notes collection.
    todos = get_reference_to_todos_collection()

    # Loop through all child notes of the collection. This is done in two steps:
    # 1) Loop through the keys of the child notes.
    # 2) For each key, find the actual contents.
    child_query = todos.order_by_key()
    query_iterator = child_query.get()

    # 1) Loop through the keys.
    for node_id in query_iterator:
        # 2) Fetch the actual node object.
        n = todos.child(node_id).get()
        if n[ORDINAL] == ordinal:
            todos.child(node_id).delete()
            break

def generate_todo_entry_dict(todo, ordinal):
    todo_dict = {}
    todo_dict[ORDINAL] = ordinal
    todo_dict[TODO] = todo
    return todo_dict

def add_todo_to_firebase(todo, ordinal):
    todo_dict = generate_todo_entry_dict(todo, ordinal)
    todos = get_reference_to_todos_collection()
    todos.push(todo_dict)

def read_current_todos_from_firebase():
    todos_to_return = list()

    # Get a ref to the todos collection.
    todos = get_reference_to_todos_collection()

    # Loop through all child todos of the collection. This is done in two steps:
    # 1) Loop through the keys of the child todos.
    # 2) For each key, find the actual contents.
    child_query = todos.order_by_key()
    query_iterator = child_query.get()

    # 1) Loop through the keys.
    for node_id in query_iterator:
        # 2) Fetch the actual node object.
        todo = todos.child(node_id).get()
        todos_to_return.append(todo)
    return todos_to_return

def print_todos(todos):
    print("*** TODO: ")
    if todos != None:
        for todo in todos:
            print("[" + str(todo[ORDINAL]) + "]" + " " + todo[TODO])

def get_highest_ordinal_from_todos(todos):
    if todos == None:
        return 0    
    highest_so_far = 0
    for todo in todos:
        if todo[ORDINAL] > highest_so_far:
            highest_so_far = todo[ORDINAL]
    return highest_so_far
                                    
def get_todos_from_user():
    todos = list()
    try:
        while True:
            todo = input("Please enter TODO: End with ctrl+d. : ")
            todos.append(todo)
    except EOFError:
        print() # To let the output start on a new line.
    return todos
        
def add_new_todos_to_firebase(todos, currently_highest_ordinal):
    next_ordinal = currently_highest_ordinal + 1
    for todo in todos:
        add_todo_to_firebase(todo, next_ordinal)
        next_ordinal += 1

def extract_existing_ordinals(todos_from_firebase):
    existing_ordinals = list()
    if todos_from_firebase != None:
        for todo in todos_from_firebase:
            existing_ordinals.append(todo[ORDINAL])
    
    return existing_ordinals

def ask_user_to_delete_a_todo(todos_from_firebase):
    existing_ordinals = extract_existing_ordinals(todos_from_firebase)
    done = False
    while not done:
        try:
            ordinal_to_remove_as_string = input("Enter the number of the TODO entry to remove. End with ctrl+d. : ")
            ordinal_to_remove = int(ordinal_to_remove_as_string)
            if ordinal_to_remove in existing_ordinals:
                delete_todo_from_database(ordinal_to_remove)
            else:
                print("Please specify an existing number!")                
        except ValueError:
            print("Please specify a valid number!")
        except EOFError:
            done = True
            print() # To let the output start on a new line.
    
def main():
    initialize_database_connection()
    new_todos = get_todos_from_user()
    already_existing_todos = read_current_todos_from_firebase()
    currently_highest_ordinal = get_highest_ordinal_from_todos(already_existing_todos)
    add_new_todos_to_firebase(new_todos, currently_highest_ordinal)
    todos_from_firebase = read_current_todos_from_firebase()
    print_todos(todos_from_firebase)
    if todos_from_firebase != None:
        ask_user_to_delete_a_todo(todos_from_firebase)
    
    
### MAIN ###

if __name__ == '__main__':
    main()

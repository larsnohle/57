#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import datetime
import json

import urllib.request
import urllib.parse
from urllib.request import Request, urlopen

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# CONSTANTS
NEW = 'new'
SHOW = 'show'
SEARCH = 'search'

TIMESTAMP = 'timestamp'
NOTE = 'note'
DATABASE_SERVICE_URL='https://fiftyone-a1bf4.firebaseio.com/notes.json'
TIMESTAMP_PATTERN = '{0:%Y-%m-%d %H:%M:%S}'

def generate_timestamp_string():
    return TIMESTAMP_PATTERN.format(datetime.datetime.now())

def generate_note_dict(text_to_add):
    timestamp = generate_timestamp_string()
    note_dict = {}
    note_dict[TIMESTAMP] =  timestamp
    note_dict[NOTE] = text_to_add
    return note_dict
    
def get_reference_to_notes_collection():
    # Retrieve credentials.
    cred = credentials.Certificate('./fiftyone-a1bf4-firebase-adminsdk-plp8l-d4e881d092.json')
    
    # Initialize the API so that it points to the database we want to use. Supply the credentials we just read.
    firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://fiftyone-a1bf4.firebaseio.com'
    })

    # Get a ref to the notes collection.
    notes = db.reference('notes')
    return notes

def add_note(text_to_add):
    print('Will add "%s"' % text_to_add)
    note_dict = generate_note_dict(text_to_add)

    notes = get_reference_to_notes_collection()
    notes.push(note_dict)
    
    #    print("Payload: %s" % note_dict_as_json_string)
    print("Your note was saved.")

def show_notes():
    notes = retrieve_data_from_database()
    for note in notes:
        print(note[TIMESTAMP] + " " + note[NOTE])

def search_notes(text_to_search_for):
    notes = retrieve_data_from_database()
    for note in notes:
        if text_to_search_for in note[TIMESTAMP] or text_to_search_for in note[NOTE]:
            print(note[TIMESTAMP] + " " + note[NOTE])

def retrieve_data_from_database():
    data = list()

    # Get a ref to the notes collection.
    notes = get_reference_to_notes_collection()

    # Loop through all child notes of the collection. This is done in two steps:
    # 1) Loop through the keys of the child notes.
    # 2) For each key, find the actual contents.
    child_query = notes.order_by_key()
    query_iterator = child_query.get()

    # 1) Loop through the keys.
    for node_id in query_iterator:
        # 2) Fetch the actual node object.
        n = notes.child(node_id).get()
        data.append(n)
    return data
            
def main():        
    if len(sys.argv) < 2:
        print("USAGE: python3 fiftyOne.py command [options]")
        sys.exit(1)

    command = sys.argv[1]
    parameters = None
    paramenters_joined = None

    if len(sys.argv) > 2:
        parameters = sys.argv[2:]
        paramenters_joined = ' '.join(parameters)
        
    if command == NEW and (parameters == None or len(parameters) == 0):
        print("USAGE: python3 fiftyOne.py new text to insert")
        sys.exit(1)
    elif command == SEARCH and (parameters == None or len(parameters) == 0):
        print("USAGE: python3 fiftyOne.py search text to search for")
        sys.exit(1)
        
    if command == NEW:
        add_note(paramenters_joined)
    elif command == SHOW:
        show_notes()
    elif command == SEARCH:
        search_notes(paramenters_joined)
    else:
        print("Unknown command '%s'" % command)
        sys.exit(1)
    
        
### MAIN ###

if __name__ == '__main__':
    main()

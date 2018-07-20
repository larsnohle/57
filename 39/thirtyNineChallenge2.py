#!/usr/bin/python3
# -*- coding: utf-8 -*-

#db.employee.insert({"firstName": "John", "lastName":"Johnson", "position":"Manager", "separationDate":"2016-12-31"})
#db.employee.insert({"firstName": "Tou", "lastName":"Xiong", "position":"Software Engineer", "separationDate":"2016-10-05"})
#db.employee.insert({"firstName": "Michaela", "lastName":"Michaelson", "position":"District Manager", "separationDate":"2015-12-19"})
#db.employee.insert({"firstName": "Jake", "lastName":"Jacobson", "position":"Programmer"})
#db.employee.insert({"firstName": "Jacquelyn", "lastName":"Jackson", "position":"DBA"})
#db.employee.insert({"firstName": "Sally", "lastName":"Weber", "position":"Web Developer", "separationDate":"2015-12-18"})

#John Johnson Manager 2016-12-31
#Tou Xiong Software Engineer 2016-10-05
#Michaela Michaelson District Manager 2015-12-19
# Jake Jacobson Programmer
#Jacquelyn Jackson DBA
#Sally Weber Web Developer 2015-12-18

from pymongo import MongoClient

persons = list()

FIRST_NAME = "firstName"
LAST_NAME = "lastName"
POSITION = "position"
SEPARATION_DATE = "separationDate"
persons.append({FIRST_NAME : "John", LAST_NAME: "Johnson", POSITION: "Manager", SEPARATION_DATE: "2016-12-31"})
persons.append({FIRST_NAME : "Tou", LAST_NAME: "Xiong", POSITION: "Software Engineer", SEPARATION_DATE: "2016-10-05"})
persons.append({FIRST_NAME : "Michaela", LAST_NAME: "Michaelson", POSITION: "District Manager", SEPARATION_DATE: "2015-12-19"})
persons.append({FIRST_NAME : "Jake", LAST_NAME: "Jacobson", POSITION: "Programmer"})
persons.append({FIRST_NAME : "Jacquelyn", LAST_NAME: "Jackson", POSITION: "DBA"})
persons.append({FIRST_NAME : "Sally", LAST_NAME: "Weber", POSITION: "Web Developer", SEPARATION_DATE: "2015-12-18"})

NAME_COLUMN_TITLE = "Name"
POSITION_COLUMN_TITLE = "Position" 
SEPARATION_DATE_COLUMN_TITLE = "Separation Date" 

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def sort_based_on_separation_date():
    return sort_based_on_attribute(SEPARATION_DATE)

def sort_based_on_position():
    return sort_based_on_attribute(POSITION)

def sort_based_on_last_name():
    return sort_based_on_attribute(LAST_NAME)

def sort_based_on_attribute(attribute):
    sorted_persons = list()
    
    sorted_persons.append(persons[0])
    index = 1
    while index < len(persons):
        j = 0
        person_to_insert = persons[index]
        insertion_position_found = False
        while insertion_position_found == False and j < len(sorted_persons):
            if attribute not in person_to_insert or (attribute in sorted_persons[j] and person_to_insert[attribute] < sorted_persons[j][attribute]):
                insertion_position_found = True
                sorted_persons.insert(j, person_to_insert)
            j += 1

        if insertion_position_found == False:
            sorted_persons.append(person_to_insert)
        index += 1
    return sorted_persons


def calculate_column_widths(length_of_longest_name, length_of_longest_position, length_of_longest_separation_date):
    name_column_width = max(len(NAME_COLUMN_TITLE), length_of_longest_name) + 2 # +1 for the space between first name and last name, +1 for the trailing space.
    position_column_width = max(len(POSITION_COLUMN_TITLE), length_of_longest_position) + 2 # +1 for the leading space +1 for the trailing space.
    separation_date_column_width = max(len(SEPARATION_DATE_COLUMN_TITLE), length_of_longest_separation_date) + 1 # +1 for the trailing space.

    return (name_column_width, position_column_width, separation_date_column_width)
    
def print_header(name_column_width, position_column_width, separation_date_column_width):
    print(NAME_COLUMN_TITLE, end='')
    print(" " * (name_column_width - len(NAME_COLUMN_TITLE)), end='')
    print("| ", end='')
    print(POSITION_COLUMN_TITLE, end='')
    print(" " * (position_column_width - len(POSITION_COLUMN_TITLE) - 1), end='') # -1 because one space is included in "| "
    print("| ", end='')
    print(SEPARATION_DATE_COLUMN_TITLE, end='')
    print(" " * (separation_date_column_width - len(SEPARATION_DATE_COLUMN_TITLE) -1))

    print("-" * name_column_width, end='')
    print("|", end='')
    print("-" * position_column_width, end='')
    print("|", end='')
    print("-" * separation_date_column_width)

def print_person(person, name_column_width, position_column_width, separation_date_column_width):
    name = person[FIRST_NAME] + " " + person[LAST_NAME]
    position = person[POSITION]
    separation_date = ""
    if SEPARATION_DATE in person:
        separation_date = person[SEPARATION_DATE]
    print(name, end='')
    print(" " * (name_column_width - len(name)), end='')
    print("| ", end='')
    print(position, end='')
    print(" " * (position_column_width - len(position) - 1), end='') # -1 because one space is included in "| "
    print("| ", end='')
    print(separation_date)

def length_of_longest_name():
    max_so_far = 0
    for person in persons:
        name_len = len(person[FIRST_NAME]) + len(person[LAST_NAME])
        if name_len > max_so_far:
            max_so_far = name_len
    return max_so_far
          
def length_of_longest_attribute_value_of_person(attribute):
    max_so_far = 0
    for person in persons:
        if attribute in person:
            attribute_value_len = len(person[attribute])
            if attribute_value_len > max_so_far:
                max_so_far = attribute_value_len
    return max_so_far

def length_of_longest_position():
    return length_of_longest_attribute_value_of_person(POSITION)

def length_of_longest_separation_date():
    return length_of_longest_attribute_value_of_person(SEPARATION_DATE)

def read_data_from_db():
    client = MongoClient('localhost', 27017)
    db = client.exercisesForProgrammers
    employees = db.employees
    persons = employees.find()

def main():
    read_data_from_db()
    
    sorted_persons = None
    choice = get_string_input("Sort on separation date(s), position(p) or last name(l)? ", ['s', 'p', 'l'])
    if choice == 's':
        sorted_persons = sort_based_on_separation_date()
    elif choice == 'p':
        sorted_persons = sort_based_on_position()
    elif choice == 'l':
        sorted_persons = sort_based_on_last_name()
    else:
        print("Incorrect choice!") # Should not happen.

    (name_column_width, position_column_width, separation_date_column_width) = calculate_column_widths(length_of_longest_name(), length_of_longest_position(), length_of_longest_separation_date())
    print_header(name_column_width, position_column_width, separation_date_column_width)
    for person in sorted_persons:
        print_person(person, name_column_width, position_column_width, separation_date_column_width)
    
### MAIN ###

if __name__ == '__main__':
    main()

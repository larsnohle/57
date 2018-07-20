#!/usr/bin/python3
# -*- coding: utf-8 -*-

#from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta # From the package python-dateutil which I've installed using pip3.

persons = list()

#John Johnson Manager 2016-12-31
#Tou Xiong Software Engineer 2016-10-05
#Michaela Michaelson District Manager 2015-12-19
# Jake Jacobson Programmer
#Jacquelyn Jackson DBA
#Sally Weber Web Developer 2015-12-18

FILENAME = "persons.txt"

NAME_COLUMN_TITLE = "Name"
POSITION_COLUMN_TITLE = "Position" 
SEPARATION_DATE_COLUMN_TITLE = "Separation Date" 

ENTER_SEARCH_STRING = "Enter a search string: "

FIRST_NAME = "firstName"
LAST_NAME = "lastName"
POSITION = "position"
SEPARATION_DATE = "separationDate"

def read_data_from_file():
    with open(FILENAME, 'r') as f:
        for line in f:
            person_dict = dict()
            line = line.strip()
            fields = line.split(',')
            if len(fields) < 3:
                print("The following row in the indata file %s is malformed: " % FILENAME)
                print(line)
                continue
            
            person_dict[FIRST_NAME] = fields[0].strip()
            person_dict[LAST_NAME] = fields[1].strip()
            person_dict[POSITION] = fields[2].strip()

            if len(fields) >= 4:
                person_dict[SEPARATION_DATE] = fields[3].strip()

            persons.append(person_dict)

def get_string_to_search_for():
    s = input(ENTER_SEARCH_STRING)
    return s

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def filter_on_name(search_string):
    filtered_persons = list()
    search_string = search_string.upper()
    for person in persons:
        if search_string in person[FIRST_NAME].upper() or search_string in person[LAST_NAME].upper():
            filtered_persons.append(person)
    return filtered_persons

def filter_on_position(search_string):
    filtered_persons = list()
    search_string = search_string.upper()
    for person in persons:
        if search_string in person[POSITION].upper():
            filtered_persons.append(person)
    return filtered_persons

def filter_on_separation_date_more_than_six_months_ago():
    filtered_persons = list()
    now = datetime.datetime.now()
    for person in persons:
        if SEPARATION_DATE in person:            
            separation_date = datetime.datetime.strptime(person[SEPARATION_DATE], '%Y-%m-%d')
            six_months_ago = now - relativedelta(months = 6)
            if separation_date < six_months_ago:
                filtered_persons.append(person)
    return filtered_persons
                
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

def length_of_longest_name(person_list):
    max_so_far = 0
    for person in person_list:
        name_len = len(person[FIRST_NAME]) + len(person[LAST_NAME])
        if name_len > max_so_far:
            max_so_far = name_len
    return max_so_far
          
def length_of_longest_attribute_value_of_person(attribute, person_list):
    max_so_far = 0
    for person in person_list:
        if attribute in person:
            attribute_value_len = len(person[attribute])
            if attribute_value_len > max_so_far:
                max_so_far = attribute_value_len
    return max_so_far

def length_of_longest_position(person_list):
    return length_of_longest_attribute_value_of_person(POSITION, person_list)

def length_of_longest_separation_date(person_list):
    return length_of_longest_attribute_value_of_person(SEPARATION_DATE, person_list)
          
def main():
    read_data_from_file()
    choice = get_string_input("Filter on name(n), position(p) or on separation date > 6 months(s)? ", ['n', 'p', 's'])
    if choice == 'n':
        filtered_persons = filter_on_name(get_string_to_search_for())
    elif choice == 'p':
        filtered_persons = filter_on_position(get_string_to_search_for())
    elif choice == 's':
        filtered_persons = filter_on_separation_date_more_than_six_months_ago()
    else:
        print("Incorrect choice!") # Should not happen.
    
    (name_column_width, position_column_width, separation_date_column_width) = calculate_column_widths(length_of_longest_name(filtered_persons), length_of_longest_position(filtered_persons), length_of_longest_separation_date(filtered_persons))
    print_header(name_column_width, position_column_width, separation_date_column_width)
    for person in filtered_persons:
        print_person(person, name_column_width, position_column_width, separation_date_column_width)
    
### MAIN ###

if __name__ == '__main__':
    main()

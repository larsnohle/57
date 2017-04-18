#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import datetime
from datetime import date
from datetime import timedelta
import re

FIRST_NAME = "firstName"
LAST_NAME = "lastName"
NAME = "Name"
POSITION = "position"
SEPARATION_DATE = "separationDate"

DATE_REG_EXP = re.compile("(\\d\\d\\d\\d)-(\\d\\d)-(\\d\\d)")

FILENAME = 'employees.txt'
#ROW_INCL_SEPARATION_DATE_REG_EXP = re.compile("(\\w+),(\\w+),(\\w+),(\\d\\d\\d\\d-\\d\\d-\\d\\d)")
ROW_INCL_SEPARATION_DATE_REG_EXP = re.compile("(.+),(.+),(.+),(\\d\\d\\d\\d-\\d\\d-\\d\\d)")
ROW_NOT_INCL_SEPARATION_DATE_REG_EXP = re.compile("(.+),(.+),(.+)")

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def print_character_repeatedly(char, number_of_times_to_print):
    for i in range(0, number_of_times_to_print):
            print(char, end='')

def print_header(len_of_longest_name, len_of_longest_position, len_of_longest_separation_date):
    print(NAME, end='')
    print_character_repeatedly(' ', len_of_longest_name - len('Name') + 1)
    print('|', end='')
    print(' ', end='')
    print(POSITION, end='')
    print_character_repeatedly(' ', len_of_longest_position - len('Position') + 1)
    print('|', end='')
    print(' ', end='')
    print(SEPARATION_DATE, end='')
    print("")

    print_character_repeatedly('-', len_of_longest_name + 1)
    print('|', end='')
    print_character_repeatedly('-', len_of_longest_position + 2)
    print('|', end='')
    print_character_repeatedly('-', len_of_longest_separation_date + 1)
    print("")
    
def print_person(person, len_of_longest_name, len_of_longest_position, len_of_longest_separation_date):
    name = "%s %s"% (person[FIRST_NAME], person[LAST_NAME])
    print(name, end='')
    print_character_repeatedly(' ', len_of_longest_name - len(name) + 1)
    print('|', end='')
    print(' ', end='')
    print(person[POSITION], end='')
    print_character_repeatedly(' ', len_of_longest_position - len(person[POSITION]) + 1)
    print('|', end='')
    print(' ', end='')
    if SEPARATION_DATE in person:
        print(person[SEPARATION_DATE], end='')
    print("")

def length_of_longest(persons, key):
    max_so_far = 0
    for person in persons:
        if key in person and len(person[key]) > max_so_far:
            max_so_far = len(person[key])
    return max_so_far
            
def longest_name(persons):
    max_so_far = 0
    for person in persons:
        l = len(person[FIRST_NAME]) + len(person[LAST_NAME])
        if l > max_so_far:
            max_so_far = l
    return max_so_far

def longest_position(persons):
    return length_of_longest(persons, POSITION)

def longest_separation_date(persons, ):
    return length_of_longest(persons, SEPARATION_DATE)

def read_persons():
    persons = list()

    f = open(FILENAME, 'r')
    for row in f:
        row_groups = None
        
        match = ROW_INCL_SEPARATION_DATE_REG_EXP.search(row)
        
        if match != None: 
            row_groups = match.groups()
        else:
            match = ROW_NOT_INCL_SEPARATION_DATE_REG_EXP.search(row)
            if match != None: 
                row_groups = match.groups()

        if row_groups != None:
                first_name = row_groups[0]
                last_name = row_groups[1]
                position  = row_groups[2]
            
        if len(row_groups) > 3:
            separation_date = row_groups[3]
            persons.append({FIRST_NAME : first_name, LAST_NAME: last_name, POSITION: position, SEPARATION_DATE: separation_date})
        else:
            persons.append({FIRST_NAME : first_name, LAST_NAME: last_name, POSITION: position})
                
    return persons

def filter(persons, search_string, fields_to_filter_on):
    filtered_persons = list()
    search_string = search_string.upper()

    for person in persons:
        for field_to_filter_on in fields_to_filter_on:
            if field_to_filter_on in person and person[field_to_filter_on] != None and search_string in person[field_to_filter_on].upper():
                filtered_persons.append(person)
                break

    return filtered_persons

def date_as_string_groups_to_date(date_field_groups):
    if len(date_field_groups) != 3:
        return None

    year_as_string = date_field_groups[0]
    month_as_string = date_field_groups[1]
    day_as_string = date_field_groups[2]

    year = int(year_as_string)
    
    month = None
    if month_as_string[0] == '0':
        month = int(month_as_string[1])
    else:
        month = int(month_as_string)

    day = None
    if day_as_string[0] == '0':
        day = int(day_as_string[1])
    else:
        day = int(day_as_string)
        
    return date(year, month, day) 
    

def filter_previous_employees(persons):
    filtered_persons = list()
    today = date.today()
    delta = timedelta(weeks=26)
    separation_date = date(2016, 8, 17)
    for person in persons:
        if SEPARATION_DATE in person:
            separation_date_as_string = person[SEPARATION_DATE]
            date_field_groups = DATE_REG_EXP.search(separation_date_as_string).groups()
            if len(date_field_groups) == 3:
                separation_date = date_as_string_groups_to_date(date_field_groups)
                six_months_ago = today - delta

                if separation_date < six_months_ago:
                    filtered_persons.append(person)
    return filtered_persons
                    
def main():
    persons = read_persons()
    field_to_filter_on = get_string_input("Please select field to filter on name(n), position(p), separation date more than six months (s): ", ['n', 'p', 's'])

    filtered_persons = None
    if field_to_filter_on == 'n':
        search_string = input("Enter a search string: ")
        filtered_persons = filter(persons, search_string, [FIRST_NAME, LAST_NAME])
    elif field_to_filter_on == 'p':
        search_string = input("Enter a search string: ")
        filtered_persons = filter(persons, search_string, [POSITION])
    elif field_to_filter_on == 's':
        filtered_persons = filter_previous_employees(persons)        
    
    len_of_longest_name = longest_name(filtered_persons)
    len_of_longest_position = longest_position(filtered_persons)
    len_of_longest_separation_date = longest_separation_date(filtered_persons)

    # The string 'Separation date' might be longer than the longest separation date value.
    if len(SEPARATION_DATE) > len_of_longest_separation_date:
        len_of_longest_separation_date = len(SEPARATION_DATE)
    
    print_header(len_of_longest_name, len_of_longest_position, len_of_longest_separation_date)
    for person in filtered_persons:
        print_person(person, len_of_longest_name, len_of_longest_position, len_of_longest_separation_date)
    
### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

FIRST_NAME = "firstName"
LAST_NAME = "lastName"
NAME = "Name"
POSITION = "position"
SEPARATION_DATE = "separationDate"


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
    persons.append({FIRST_NAME : "John", LAST_NAME: "Johnson", POSITION: "Manager", SEPARATION_DATE: "2016-12-31"})
    persons.append({FIRST_NAME : "Tou", LAST_NAME: "Xiong", POSITION: "Software Engineer", SEPARATION_DATE: "2016-10-05"})
    persons.append({FIRST_NAME : "Michaela", LAST_NAME: "Michaelson", POSITION: "District Manager", SEPARATION_DATE: "2015-12-19"})
    persons.append({FIRST_NAME : "Jake", LAST_NAME: "Jacobson", POSITION: "Programmer"})
    persons.append({FIRST_NAME : "Jacquelyn", LAST_NAME: "Jackson", POSITION: "DBA"})
    persons.append({FIRST_NAME : "Sally", LAST_NAME: "Weber", POSITION: "Web Developer", SEPARATION_DATE: "2015-12-18"})

    return persons

def filter(persons, search_string):
    filtered_persons = list()
    search_string = search_string.upper()
    for person in persons:
        if search_string in person[FIRST_NAME].upper() or search_string in person[LAST_NAME].upper():
            filtered_persons.append(person)

    return filtered_persons

def main():
    persons = read_persons()
    search_string = input("Enter a search string:")

    filtered_persons = filter(persons, search_string)
    
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

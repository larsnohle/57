#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

FIRST_NAME = "firstName"
LAST_NAME = "lastName"
NAME = "Name"
POSITION = "position"
SEPARATION_DATE = "separationDate"

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def sort(persons, field_to_sort_on):
    sorted_persons = list()
    
    sorted_persons.append(persons[0])
    index = 1
    while index < len(persons):
        j = 0
        person_to_insert = persons[index]
        insertion_position_found = False
        field_of_person_to_insert = None
        if field_to_sort_on in person_to_insert:
            field_of_person_to_insert = person_to_insert[field_to_sort_on]        

        # If the field is None => append last.
        if field_of_person_to_insert != None:
            while insertion_position_found == False and j < len(sorted_persons):
                field_of_sorted_person = sorted_persons[j][field_to_sort_on]

                # If we've found a None field in the list we want to sort our person before.
                if field_of_sorted_person == None or field_of_person_to_insert < field_of_sorted_person:
                    insertion_position_found = True
                    sorted_persons.insert(j, person_to_insert)

                j += 1

        if insertion_position_found == False:
            sorted_persons.append(person_to_insert)
        index += 1
    return sorted_persons


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

def read_persons_from_db():
    persons = list()
    client = MongoClient()
    db = client.exercise39of57
    employees = db.employees.find()
    persons.extend(employees)

    return persons

def main():
    persons = read_persons_from_db()
    field_to_sort_on = get_string_input("Please select field to sort on (f, l, p, s): ", ['f','l','p','s'])

    if field_to_sort_on == 'f':
        sorted_persons = sort(persons, FIRST_NAME)
    elif field_to_sort_on == 'l':
        sorted_persons = sort(persons, LAST_NAME)
    elif field_to_sort_on == 'p':
        sorted_persons = sort(persons, POSITION)
    elif field_to_sort_on == 's':
        sorted_persons = sort(persons, SEPARATION_DATE)
    else:
        print("Something is rotten in the state of Denmark.")
        
    len_of_longest_name = longest_name(persons)
    len_of_longest_position = longest_position(persons)
    len_of_longest_separation_date = longest_separation_date(persons)

    # The string 'Separation date' might be longer than the longest separation date value.
    if len(SEPARATION_DATE) > len_of_longest_separation_date:
        len_of_longest_separation_date = len(SEPARATION_DATE)
    
    print_header(len_of_longest_name, len_of_longest_position, len_of_longest_separation_date)
    for person in sorted_persons:
        print_person(person, len_of_longest_name, len_of_longest_position, len_of_longest_separation_date)
    
### MAIN ###

if __name__ == '__main__':
    main()

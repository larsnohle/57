#!/usr/bin/python3
# -*- coding: utf-8 -*-

# THIS IS PROBLEM 41 REWRITTEN TO USE FIREBASE.
# THE SORTED ENTRIES ARE STILL WRITTEN TO A FILE AS firebase would still mess up the order. All entries could iofs be stored as a single entry in firebase, but orkar inte.
import datetime
import json

import urllib.request
import urllib.parse
from urllib.request import Request, urlopen

DATABASE_SERVICE_URL_READ='https://fiftyone-a1bf4.firebaseio.com/fortyOneUnsorted.json'

OUT_FILENAME = "personsSorted.txt"

FIRST_NAME = "firstName"
LAST_NAME = "lastName"

def generate_person_in_json_format(first_name, last_name):
    person_dict = {}
    person_dict[FIRST_NAME] =  first_name
    person_dict[LAST_NAME] =  last_name
    return json.dumps(person_dict)


def perform_initial_load():
    in_filename = "persons.txt"
    with open(in_filename, 'r') as f:
        for line in f:
            line = line.strip()
            fields = line.split(',')
            if len(fields) < 2:
                print("The following row in the indata file %s is malformed: " % line)
                print(line)
                continue
            
            last_name = fields[0].strip()
            first_name = fields[1].strip()
            
            print('Will add last_name: %s first_name: %s ' % (last_name, first_name))
            person_dict_as_json_string = generate_person_in_json_format(first_name, last_name)
            print("Payload: %s" % person_dict_as_json_string)
    
            request = Request(DATABASE_SERVICE_URL_READ, person_dict_as_json_string.encode())
            response_payload = urlopen(request).read().decode()
#    print("Response: ")
#    print(response_payload)
    print("The persons were saved in the unsorted collection.")


def write_data_to_file(persons):
    with open(OUT_FILENAME, 'w') as f:
        for person in persons:
            f.write(person[LAST_NAME])
            f.write(', ')
            f.write(person[FIRST_NAME])
            f.write('\n')

def read_data_from_database():
    persons = list()
    request = Request(DATABASE_SERVICE_URL_READ)
    response_payload = urlopen(request).read().decode()
    person_entry_dict = json.loads(response_payload)
    for v in person_entry_dict.values():
        person_dict = dict()
        person_dict[LAST_NAME] = v[LAST_NAME]
        person_dict[FIRST_NAME] = v[FIRST_NAME]
        persons.append(person_dict)
    return persons


def sort_persons(persons):
    sorted_persons = list()

    for person in persons:
        for (index, p2) in enumerate(sorted_persons):
            if person[LAST_NAME] < p2[LAST_NAME] or (person[LAST_NAME] == p2[LAST_NAME] and person[FIRST_NAME] < p2[FIRST_NAME]):
                sorted_persons.insert(index, person)
                break
        else:
            sorted_persons.append(person)
            
    return sorted_persons

def print_persons(persons):
    header_first_row = "Total of %d names" % len(persons)
    header_second_row = '-' * (len(header_first_row) + 1)
    print(header_first_row)
    print(header_second_row)

    for person in persons:
        print(person[LAST_NAME], end='')
        print(', ', end='')
        print(person[FIRST_NAME])
        
def main():
    #perform_initial_load()
    persons = read_data_from_database()
    #print(persons)
    sorted_persons = sort_persons(persons)
    print_persons(sorted_persons)
    write_data_to_file(sorted_persons)
    
### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import datetime
import json

import urllib.request
import urllib.parse
from urllib.request import Request, urlopen

# CONSTANTS
NEW = 'new'
SHOW = 'show'
TIMESTAMP = 'timestamp'
NOTE = 'note'
DATABASE_SERVICE_URL='https://fiftyone-a1bf4.firebaseio.com/notes.json'
TIMESTAMP_PATTERN = '{0:%Y-%m-%d %H:%M:%S}'


def generate_timestamp_string():
    return TIMESTAMP_PATTERN.format(datetime.datetime.now())

def generate_note_in_json_format(text_to_add):
    timestamp = generate_timestamp_string()
    note_dict = {}
    note_dict[TIMESTAMP] =  timestamp
    note_dict[NOTE] = text_to_add
    return json.dumps(note_dict)

def add_note(text_to_add):
    print('Will add "%s"' % text_to_add)
    note_dict_as_json_string = generate_note_in_json_format(text_to_add)
#    print("Payload: %s" % note_dict_as_json_string)
    
    request = Request(DATABASE_SERVICE_URL, note_dict_as_json_string.encode())
    response_payload = urlopen(request).read().decode()
#    print("Response: ")
#    print(response_payload)
    print("Your note was saved.")

def show_notes():
    request = Request(DATABASE_SERVICE_URL)
    response_payload = urlopen(request).read().decode()
#    print("Response: ")
#    print(response_payload)
    notes_dict = json.loads(response_payload)
    for v in notes_dict.values():
        print(v[TIMESTAMP] + " " + v[NOTE])
   
def main():
    if len(sys.argv) < 2:
        print("USAGE: python3 fiftyOne.py command [options]")
        sys.exit(1)

    command = sys.argv[1]
    parameters = None

    if len(sys.argv) > 2:
        parameters = sys.argv[2:]
        
    if command == NEW and (parameters == None or len(parameters) == 0):
        print("USAGE: python3 fiftyOne.py new text to insert")
        sys.exit(1)

    if command == NEW:
        text_to_add = ' '.join(parameters)
        add_note(text_to_add)
    elif command == SHOW:
        show_notes()
    else:
        print("Unknown command '%s'" % command)
        sys.exit(1)
    
        
### MAIN ###

if __name__ == '__main__':
    main()

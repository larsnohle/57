#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyzåäö"
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 10
NUMBER_OF_NAMES_TO_GENERATE = 10000

OUT_FILE_NAME = "manyPersons.txt" 

def generate_name():
    length_of_name_to_generate = random.randint(MIN_NAME_LENGTH, MAX_NAME_LENGTH)
    name = ''.join([random.choice(LOWER_CASE_LETTERS) for x in range(length_of_name_to_generate + 1)])
    name = name[0].upper() + name [1:]
    return name

def main():
    with open(OUT_FILE_NAME, 'w') as f:
        for i in range(NUMBER_OF_NAMES_TO_GENERATE):
            last_name = generate_name()
            first_name = generate_name()
            f.write(last_name)
            f.write(', ')
            f.write(first_name)
            f.write('\n')

### MAIN ###

if __name__ == '__main__':
    main()

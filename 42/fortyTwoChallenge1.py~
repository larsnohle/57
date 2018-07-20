#!/usr/bin/python3
# -*- coding: utf-8 -*-

# CONSTANTS
IN_FILE_NAME = 'dataFile.csv'
LAST_NAME = 'LAST_NAME'
FIRST_NAME = 'FIRST_NAME'
SALARY = 'SALARY'
LAST_COLUMN_TITLE = 'Last'
FIRST_COLUMN_TITLE = 'First'
SALARY_COLUMN_TITLE = 'Salary'

def read_file():
    persons = list()
    with open(IN_FILE_NAME, 'r') as f:
        for line in f:
            line = line.strip()
            fields = line.split(',')
            if len(fields) != 3:
                print('Incorrect data format!')
                continue
            person_dict = dict()
            person_dict[LAST_NAME] =  fields[0]
            person_dict[FIRST_NAME] =  fields[1]
            person_dict[SALARY] =  fields[2]
            persons.append(person_dict)
    return persons

def calculate_column_widths(persons):
    length_of_longest_last_name = 0
    length_of_longest_first_name = 0
    length_of_longest_salary = 0

    for person in persons:
        if len(person[LAST_NAME]) > length_of_longest_last_name:
            length_of_longest_last_name = len(person[LAST_NAME])

        if len(person[FIRST_NAME]) > length_of_longest_first_name:
            length_of_longest_first_name = len(person[FIRST_NAME])

        if len(person[SALARY]) > length_of_longest_salary:
            length_of_longest_salary = len(person[SALARY])

    return (length_of_longest_last_name + 1, length_of_longest_first_name + 1, length_of_longest_salary + 1)


def print_header(column_widths):
    last_name_col_width, first_name_col_width, salary_col_width = column_widths
    print(LAST_COLUMN_TITLE, end = '')
    print(' ' * (last_name_col_width - len(LAST_COLUMN_TITLE)), end = '')
    print(FIRST_COLUMN_TITLE, end = '')
    print(' ' * (first_name_col_width - len(FIRST_COLUMN_TITLE)), end = '')
    print(SALARY_COLUMN_TITLE)
    print('-' * (last_name_col_width + first_name_col_width + salary_col_width))


def print_persons(persons, column_widths):
    last_name_col_width, first_name_col_width, salary_col_width = column_widths
    for person in persons:
        last_name = person[LAST_NAME]
        first_name = person[FIRST_NAME]
        salary = person[SALARY]
        print(last_name, end = '')
        print(' ' * (last_name_col_width - len(last_name)), end = '')
        print(first_name, end = '')
        print(' ' * (first_name_col_width - len(first_name)), end = '')
        print(salary)        
    
def main():
    persons = read_file()
    column_widths = calculate_column_widths(persons)
    print_header(column_widths)
    print_persons(persons, column_widths)

### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

# CONSTANTS
IN_FILE_NAME = 'dataFile.csv'
LAST_NAME = 'LAST_NAME'
FIRST_NAME = 'FIRST_NAME'
SALARY = 'SALARY'
FORMATTED_SALARY = 'FORMATTED_SALARY'
LAST_COLUMN_TITLE = 'Last'
FIRST_COLUMN_TITLE = 'First'
SALARY_COLUMN_TITLE = 'Salary'
NUMBER_OF_DIGITS_IN_SECTION = 3


def format_salary(salary):
    number_of_digits_in_salary = len(salary)

    # Check if a comma is redundant. If so just return $salary.
    if number_of_digits_in_salary <= NUMBER_OF_DIGITS_IN_SECTION:
        return '$' + salary

    # At least on comma needed.
    formatted_salary = '$'
    digits_before_first_comma = len(salary) % NUMBER_OF_DIGITS_IN_SECTION
    formatted_salary += salary[0:digits_before_first_comma]

    current_index = digits_before_first_comma
    while current_index < number_of_digits_in_salary:
        # Any digits added? If so, add a comma.
        if len(formatted_salary) > 1:
            formatted_salary += ','
        formatted_salary += salary[current_index:current_index + NUMBER_OF_DIGITS_IN_SECTION]
        current_index += NUMBER_OF_DIGITS_IN_SECTION

    return formatted_salary
    

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
            person_dict[FORMATTED_SALARY] =  format_salary(fields[2])
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

        if len(person[FORMATTED_SALARY]) > length_of_longest_salary:
            length_of_longest_salary = len(person[FORMATTED_SALARY])

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
        formatted_salary = person[FORMATTED_SALARY]
        print(last_name, end = '')
        print(' ' * (last_name_col_width - len(last_name)), end = '')
        print(first_name, end = '')
        print(' ' * (first_name_col_width - len(first_name)), end = '')
        print(formatted_salary)        
    
def main():
    persons = read_file()
    column_widths = calculate_column_widths(persons)
    print_header(column_widths)
    print_persons(persons, column_widths)

### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import re

NAME_OF_INFILE = "employees.csv"
EMPLOYEE_REG_EXP = re.compile("([^,]+),([^,]+),(\\d+)")
FIRST_NAME='First'
LAST_NAME='Last'
SALARY = 'Salary'

def read_employees(filename):
    persons = list()

    f = open(filename, 'r')
    for person in f:
        persons.append(person.strip())
    
    return persons

def split_into_fields(employee):
    employee_groups = EMPLOYEE_REG_EXP.search(employee).groups()
    return (employee_groups[0], employee_groups[1], employee_groups[2])

def len_of_longest_item(l):
    longest_so_far = -1
    for s in l:
        if len(s) > longest_so_far:
            longest_so_far = len(s)

    return longest_so_far

def print_header(width_of_last_name_column, width_of_first_name_column, width_of_salaries_column):
    print(LAST_NAME, end='')
    print(' ' * (width_of_last_name_column - len(LAST_NAME)), end='')
    print(FIRST_NAME, end='')
    print(' ' * (width_of_first_name_column - len(FIRST_NAME)), end='')
    print(SALARY)
    print("-" * (width_of_last_name_column + width_of_first_name_column + width_of_salaries_column))
    
def print_row(last_name, first_name, salary, width_of_last_name_column, width_of_first_name_column):
    print(last_name, end='')
    print(' ' * (width_of_last_name_column - len(last_name)), end='')
    print(first_name, end='')
    print(' ' * (width_of_first_name_column - len(first_name)), end='')
    print(salary)
    
def main():
    start = time.clock() 
    employees = read_employees(NAME_OF_INFILE)
    last_names = list()
    first_names = list()
    salaries = list()
    for employee in employees:
        (last_name, first_name, salary) = split_into_fields(employee)
        last_names.append(last_name)
        first_names.append(first_name)
        salaries.append(salary)


    width_of_last_name_column = len_of_longest_item(last_names) + 1
    width_of_first_name_column = len_of_longest_item(first_names) + 1
    width_of_salaries_column = len_of_longest_item(salaries) + 1    

    print_header(width_of_last_name_column, width_of_first_name_column, width_of_salaries_column)
    for i in range(0, len(employees)):
        print_row(last_names[i], first_names[i], salaries[i], width_of_last_name_column, width_of_first_name_column)
    
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in (function name) is: ", elapsed)

### MAIN ###

if __name__ == '__main__':
    main()



#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import re

import quicksort

NAME_OF_INFILE = "employees_ch2.csv"
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

def format_to_dollars(dollars):    
    number_of_digits = len(dollars)

    if number_of_digits < 4:
        return "$" + dollars
    
    s = "$"
    index_of_first_comma = number_of_digits % 3
    current_index = 0
    if index_of_first_comma != 0:
        s += dollars[0:index_of_first_comma] + ","
        current_index += index_of_first_comma

    while current_index + 3 < number_of_digits:
        s += dollars[current_index:current_index + 3] + ","
        current_index += 3

    s += dollars[current_index:]
    return s
        
    
def print_row(last_name, first_name, salary, width_of_last_name_column, width_of_first_name_column, width_of_salaries_column):
    print(last_name, end='')
    print(' ' * (width_of_last_name_column - len(last_name)), end='')
    print(first_name, end='')
    print(' ' * (width_of_first_name_column - len(first_name)), end='')
    salary = format_to_dollars(salary)
    number_of_spaces = width_of_salaries_column - len(salary)
    print(' ' * number_of_spaces, end='')
    print(salary)


def quicksort_employees_based_on_salary(l):
    number_of_items = len(l)
    if number_of_items < 2:
        return l

    # Choose last element as pivot element.
    pivot_element = l[number_of_items - 1]
    (_, _, pivot_element_salary) = pivot_element
    #   (_, _, pivot_element_salary) = pivot_element = l[number_of_items - 1] # It can also be done like this, but I think this is not as clear.

    elements_less_than_pivot = list()
    elements_greater_than_pivot = list()
    for i in range(0, number_of_items - 1):
        (last_name, first_name, salary) = l[i]
        
        if int(salary) < int(pivot_element_salary):      
            elements_less_than_pivot.append(l[i])
        else:
            elements_greater_than_pivot.append(l[i])

    sorted_lesser_elements = quicksort_employees_based_on_salary(elements_less_than_pivot)
    sorted_greater_elements = quicksort_employees_based_on_salary(elements_greater_than_pivot)

    sorted_list = list(sorted_greater_elements)    
    sorted_list.append(pivot_element)
    sorted_list.extend(sorted_lesser_elements)
    return sorted_list

def main():
    start = time.clock() 
    employees = read_employees(NAME_OF_INFILE)
    last_names = list()
    first_names = list()
    salaries = list()

    # Keep a map salary => employee dict to be able to easily sort the employees on salary.
    # Append a suffix to be handle employees having identical salaries.
    employee_tuples_list = list()
    for (index, employee) in enumerate(employees):
        (last_name, first_name, salary) = split_into_fields(employee)
        last_names.append(last_name)
        first_names.append(first_name)
        salaries.append(salary)
        employee_tuples_list.append((last_name, first_name, salary))

    width_of_last_name_column = len_of_longest_item(last_names) + 1
    width_of_first_name_column = len_of_longest_item(first_names) + 1

    # Adjust for formatting of the salary.
    width_of_salaries_column = len(format_to_dollars("1" * len_of_longest_item(salaries))) + 1

    # Sort based on salary
    sorted_employee_tuples = quicksort_employees_based_on_salary(employee_tuples_list) 

    # Print content-
    print_header(width_of_last_name_column, width_of_first_name_column, width_of_salaries_column)
    for (last_name, first_name, salary) in sorted_employee_tuples:
        print_row(last_name, first_name, salary, width_of_last_name_column, width_of_first_name_column, width_of_salaries_column)
    
    elapsed = time.clock()
    elapsed = elapsed - start
#    print("Time spent in (function name) is: ", elapsed)

### MAIN ###

if __name__ == '__main__':
    main()



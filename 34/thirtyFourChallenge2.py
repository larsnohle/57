#!/usr/bin/python3
# -*- coding: utf-8 -*-

def read_employees():
    f = open('employees.txt', 'r')

    employees = list()
    for employee in f:
        employees.append(employee.strip())

    return employees

def main():
    employees = read_employees()
    while len(employees) > 0:
        print("\nThere are %d employees: " % len(employees))
        for employee in employees:
            print(employee)
        employee_to_remove = input("Enter an employee name to remove: ")

        try:
            employees.remove(employee_to_remove)
        except ValueError:
            print("%s is not an employee!")
            
### MAIN ###

if __name__ == '__main__':
    main()




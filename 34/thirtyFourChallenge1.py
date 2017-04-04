#!/usr/bin/python3
# -*- coding: utf-8 -*-

EMPLOYEES = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]

def main():
    while len(EMPLOYEES) > 0:
        print("\nThere are %d employees: " % len(EMPLOYEES))
        for employee in EMPLOYEES:
            print(employee)
        employee_to_remove = input("Enter an employee name to remove: ")

        try:
            EMPLOYEES.remove(employee_to_remove)
        except ValueError:
            print("%s is not an employee!")
            
### MAIN ###

if __name__ == '__main__':
    main()




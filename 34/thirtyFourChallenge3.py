#!/usr/bin/python3
# -*- coding: utf-8 -*-

FILE_NAME = 'employeesChallenge3.txt'

def read_employees():
    f = open(FILE_NAME, 'r')

    employees = list()
    for employee in f:
        employees.append(employee.strip())


    f.close()
    return employees

def write_to_file(s):
    f = open(FILE_NAME, 'a')
    f.write(s)
    
def output(s):
    print(s)
    write_to_file(s + "\n")

    
def main():
    employees = read_employees()
    while len(employees) > 0:
        output("\nThere are %d employees: " % len(employees))
        for employee in employees:
            output(employee)
        employee_to_remove = input("Enter an employee name to remove: ")

        try:
            employees.remove(employee_to_remove)
        except ValueError:
            output("%s is not an employee!")
            
### MAIN ###

if __name__ == '__main__':
    main()




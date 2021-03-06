#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

MIN_FIRST_NAME_LEN = 2
MIN_LAST_NAME_LEN = 2

first_name_reg_exp = re.compile("[a-zåäöA-ZÅÄÖ][a-zåäöA-ZÅÄÖ]+")
last_name_reg_exp = re.compile("[a-zåäöA-ZÅÄÖ][a-zåäöA-ZÅÄÖ]+")
employid_reg_exp = re.compile("[a-zåäöA-ZÅÄÖ]{2}-\d\d\d\d$")
zip_code_reg_exp = re.compile("^\d+$")


def validate_minimum_string_length(a_string, min_len, field_name):
    if len(a_string) == 0:
        return "The %s must be filled in." % field_name
    elif len(a_string) < min_len:
        return "\"%s\" is not a valid %s. It is too short." % (a_string, field_name)
    return None

def validate_first_name(first_name):
    length_validation_result = validate_minimum_string_length(first_name, MIN_FIRST_NAME_LEN, "first name")

    if length_validation_result != None:
        return length_validation_result

    if first_name_reg_exp.match(first_name):
        return None 
    else:
        return "\"%s\" is not a valid first name. It must contain at least two letters." % first_name

def validate_last_name(last_name):
    length_validation_result = validate_minimum_string_length(last_name, MIN_LAST_NAME_LEN, "last name")

    if length_validation_result != None:
        return length_validation_result

    if last_name_reg_exp.match(last_name):
        return None 
    else:
        return "\"%s\" is not a valid last name. It must contain at least two letters." % last_name

def validate_employee_id(employee_id):
    ret_val = "%s is not a valid ID." % employee_id

    if len(employee_id) != 7:
        return ret_val

    if not employid_reg_exp.match(employee_id):
        return ret_val
                    
    return None

    
def validate_zip_code(zip_code):
    if not zip_code_reg_exp.match(zip_code):
        return "The ZIP code must be numeric."

    return None

def validate_input(first_name, last_name, employee_id, zip_code):
    validation_result_first_name = validate_first_name(first_name)
    validation_result_last_name = validate_last_name(last_name)
    validation_result_zip_code = validate_zip_code(zip_code)
    validation_result_employee_id = validate_employee_id(employee_id)

    if validation_result_first_name != None:
        print(validation_result_first_name)

    if validation_result_last_name != None:
        print(validation_result_last_name)

    if validation_result_employee_id != None:
        print(validation_result_employee_id)

    if validation_result_zip_code != None:
        print(validation_result_zip_code)

    if validation_result_first_name == None and validation_result_last_name == None and validation_result_employee_id == None and validation_result_zip_code == None:
        print("There were no errors found.")
    
    
def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    zip_code = input("Enter the ZIP code: ")
    employee_id = input("Enter an employee ID: ")
    validate_input(first_name, last_name, employee_id, zip_code)


### MAIN ###

if __name__ == '__main__':
    main()

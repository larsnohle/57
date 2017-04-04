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
    
def take_input_and_validate(msg, f):
    done = False
    while not done:
        inputted_string = input(msg)
        validation_result = f(inputted_string)
        if validation_result == None:
            done = True
        else:
            print(validation_result)
    
def main():
    take_input_and_validate("Enter the first name: ", validate_first_name)
    take_input_and_validate("Enter the last name: ", validate_last_name)
    take_input_and_validate("Enter the ZIP code: ", validate_zip_code)
    take_input_and_validate("Enter an employee ID: ", validate_employee_id)


### MAIN ###

if __name__ == '__main__':
    main()

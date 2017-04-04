#!/usr/bin/python3
# -*- coding: utf-8 -*-

special_characters = "! \" # $ % & \\ ' ( ) * + , - . / : ; < = > ? @ [ \ \ ] ^ _ ` { | } ~".split()

VERY_WEAK = 1
WEAK = 2
STRONG = 3
VERY_STRONG = 4
AVERAGE = 5

def contains_digit(s):
    for c in s:
        if c.isdigit():            
            return True
    return False

def contains_only_digits(s):
    for c in s:
        if not c.isdigit():
            return False
    return True

def contains_special_character(s):
    for c in s:
        if c in special_characters:
            return True
    return False

def contains_letter(s):
    for c in s:
        if c.isalpha():
            return True
    return False

def contains_only_letters(s):
    for c in s:
        if not c.isalpha():
            return False
    return True


def passwordValidator(pwd):
    if len(pwd) < 8:
        if contains_only_digits(pwd):
            return VERY_WEAK
        elif contains_only_letters(pwd):
            return WEAK
        else: # Not defined in the exercise.
            return AVERAGE
    else:
        if contains_letter(pwd) and contains_digit(pwd):
            if contains_special_character(pwd):
                return VERY_STRONG
            else:
                return STRONG
        else: # Not defined.
            return AVERAGE 
    return -1

def main():
    pwd = input("Please enter the password to be checked: ")
    rating = passwordValidator(pwd)

    rating_as_string = ""
    if rating == VERY_WEAK:
        rating_as_string = "very weak"
    elif rating == WEAK:
        rating_as_string = "weak"
    elif rating == STRONG:
        rating_as_string = "strong"
    elif rating == VERY_STRONG:
        rating_as_string = "very strong"
    elif rating == AVERAGE:
        rating_as_string = "average"
    else:
        rating_as_string = "UNDEFINED STRENGTH"

    print("The password %s is a %s password." % (pwd, rating_as_string))

### MAIN ###

if __name__ == '__main__':
    main()


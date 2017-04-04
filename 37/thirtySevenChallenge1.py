#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

DIGITS = "0123456789"
CHARACTERS = "qwertyuiopåasdfghjklläzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM"
SPECIAL_CHARACTERS = '!"#¤%&/()+@£$€¥{[]}'

def get_positive_number_input(msg, to_float = False):
    done = False
    while not done:
        try:
            i = -1.0
            if to_float == True:
                i = float(input(msg))
            else:
                i = int(input(msg))
            if i < 0:
                print("Please enter a number > 0")
            else:
                done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")

    return i

def append_special_characters(number_of_special_characters, list_to_append_to):    
    for i in range(0, number_of_special_characters):
        list_to_append_to.append(SPECIAL_CHARACTERS[random.randint(0, len(SPECIAL_CHARACTERS) - 1)])


def append_digits(number_of_digits, list_to_append_to):
    for i in range(0, number_of_digits):
        list_to_append_to.append(DIGITS[random.randint(0, len(DIGITS) - 1)])

def append_letters(number_of_characters, list_to_append_to):
    for i in range(0, number_of_characters):
        list_to_append_to.append(CHARACTERS[random.randint(0, len(CHARACTERS) - 1)])

def randBoolean():
    return random.randint(0, 1) == 1
        
def randomly_replace_vowels(list_of_characters):
    for (index, character) in enumerate(list_of_characters):
        if character == 'A' and randBoolean():
            print("Has replaced A with 4")
            list_of_characters[index] = '4'
        elif character == 'E' and randBoolean():
            list_of_characters[index] = '3'
            print("Has replaced E with 3")
        elif character == 'O' and randBoolean():
            print("Has replaced O with 0")
            list_of_characters[index] = '0'            
        
def main():
    min_len = get_positive_number_input("What's the minimum length? ")
    number_of_special_characters = get_positive_number_input("How many special characters? ")
    number_of_digits = get_positive_number_input("How many numbers? ")

    if min_len < number_of_special_characters + number_of_digits:
        print("min_len < number_of_special_characters + number_of_digits")
        return

    number_of_characters = min_len - number_of_special_characters - number_of_digits
    
    password_basic = list()
    append_special_characters(number_of_special_characters, password_basic)
    append_digits(number_of_digits, password_basic)
    append_letters(number_of_characters, password_basic)    


    # Ramdomly replace vowels.
    randomly_replace_vowels(password_basic)
    
    password = list()
    while len(password_basic) > 0:
        password.append(password_basic.pop(random.randint(0, len(password_basic) - 1)))

    print("Your password is: ")
    print(''.join(password))
        
    
### MAIN ###

if __name__ == '__main__':
    main()

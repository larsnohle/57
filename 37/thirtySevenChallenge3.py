#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from tkinter import Tk
from PyQt4 import QtGui
import pygtk
#pygtk.require('2.0')
import gtk

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
            list_of_characters[index] = '4'
        elif character == 'E' and randBoolean():
            list_of_characters[index] = '3'
        elif character == 'O' and randBoolean():
            list_of_characters[index] = '0'            

def generate_password(min_len, number_of_special_characters, number_of_digits):
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
    return ''.join(password)

def copy_string_to_clipboard(s):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(s)
    r.destroy()

def copy_to_clipboard_qt(s):
    cb = QtGui.QApplication.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText(s, mode=cb.Clipboard)

def copy_to_clipboard_gtk(s):
    clipboard = gtk.clipboard_get()
    clipboard.set_text(s)
    
def main():
    min_len = get_positive_number_input("What's the minimum length? ")
    number_of_special_characters = get_positive_number_input("How many special characters? ")
    number_of_digits = get_positive_number_input("How many numbers? ")

    if min_len < number_of_special_characters + number_of_digits:
        print("min_len < number_of_special_characters + number_of_digits")
        return

    password = generate_password(min_len, number_of_special_characters, number_of_digits)
    print("Your password is: %s" % password)
    #copy_string_to_clipboard(password)
    #copy_to_clipboard_qt(password)
    copy_to_clipboard_gtk(password)
    
### MAIN ###

if __name__ == '__main__':
    main()

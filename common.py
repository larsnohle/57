#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():

### MAIN ###

if __name__ == '__main__':
    main()


###################################################################

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


def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

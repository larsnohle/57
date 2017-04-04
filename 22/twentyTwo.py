#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

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

def numbers_are_different(number_list):
    last_index_plus_one = len(number_list)
    i = 0
    while i < last_index_plus_one:
        j = i + 1
        while j < last_index_plus_one:
            if number_list[i] == number_list[j]:
                return False
            j +=1
        i +=1

    return True


def largest_number(number_list):
    if len(number_list) == 0:
        return None

    largest_so_far = None
    for number in number_list:
        if largest_so_far == None or number > largest_so_far:
            largest_so_far = number

    return largest_so_far

def main():
    first_number = get_positive_number_input("Please enter the first number: ")
    second_number = get_positive_number_input("Please enter the second number: ")
    third_number = get_positive_number_input("Please enter the third number: ")

    number_list = []
    number_list.append(first_number)
    number_list.append(second_number)
    number_list.append(third_number)

    if numbers_are_different(number_list) == False:
        print("Not all the inputted numbers are different!")
        sys.exit()

    print("The largest number is %d." % largest_number(number_list))

### MAIN ###

if __name__ == '__main__':
    main()

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


def largest_number(number_set):
    if len(number_set) == 0:
        return None

    largest_so_far = None
    for number in number_set:
        if largest_so_far == None or number > largest_so_far:
            largest_so_far = number

    return largest_so_far

def main():
    number_set = set()

    for i in range(1, 11):
        number = get_positive_number_input("Please enter a number (%d of 10): " % i)
        while number in number_set:
            print("You have already entered that number!")
            number = get_positive_number_input("Please enter a number (%d of 10): " % i)        
        number_set.add(number)

    print("The largest number is %d." % largest_number(number_set))

### MAIN ###

if __name__ == '__main__':
    main()

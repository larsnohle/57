#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    number_of_numbers = int(input("Enter how many numbers to ask for: "))

    if number_of_numbers < 0:
        print("Incorrect number of numbers %d. Must be >= 0.")
        sys.exit(1)

    sum = 0
    for i in range(0, number_of_numbers):
        try:
            num = int(input("Enter a number: "))
            sum += num
        except ValueError:
            pass # It says to reject the bad input silently in the exercise description.

    print("The total is %d." % sum) 

### MAIN ###

if __name__ == '__main__':
    main()



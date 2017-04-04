#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
    
    i = 1
    try:
        while True:
            number = get_positive_number_input("Please enter number %d (ctrl-d to quit): " % i)
            while number in number_set:
                print("You have already entered that number!")
                number = get_positive_number_input("Please enter a number (%d): " % i)        
            number_set.add(number)
            i += 1
    except EOFError:
        pass

    print("\nThe largest number is %d." % largest_number(number_set))

### MAIN ###

if __name__ == '__main__':
    main()

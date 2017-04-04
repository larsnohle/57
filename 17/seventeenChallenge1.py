#!/usr/bin/python3
# -*- coding: utf-8 -*-

def get_positive_number_input(msg):
    done = False
    while not done:
        try:
            i = int(input(msg))
            if i <= 0:
                print("Please enter a number >= 0")
            else:
                done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")

    return i


def main():
    weight = get_positive_number_input("Weight? ")
    gender = input("Gender? ")
    number_of_drinks = get_positive_number_input("Number of standard drinks? ")
    hours = get_positive_number_input("Drinking period? ")
    
    bw = 0.58 if gender == 'M' or gender == 'm' else 0.49
    ebac = 0.806 * number_of_drinks * 1.2 / (weight * bw)  - 0.017 * hours
    
    if ebac >= 0.08:
        print("It is not legal for you to drive.")
    else:
        print("It is legal for you to drive.")

### MAIN ###

if __name__ == '__main__':
    main()

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
    bac_limit_dict = {}
    bac_limit_dict["WI"] = 0.05

    weight = get_positive_number_input("Weight? ")
    gender = input("Gender? ")
    number_of_drinks = get_positive_number_input("Number of drinks? ")
    alcohol_percent_in_drink = get_positive_number_input("Alcohol % in drink? ")
    hours = get_positive_number_input("Hours since last drink? ")
    state = input("In which state do you live? ")

    r = 0.73 if gender == 'M' or gender == 'm' else 0.66
    a = number_of_drinks * 3 * (alcohol_percent_in_drink / 100.0)
    bac = a * 5.14 / weight * r - 0.15 * hours
    #    BAC = (A × 5.14 / W × r) − .015 × H
    
    if state in bac_limit_dict:
        limit = bac_limit_dict[state]
    else:
        limit = 0.08

    if bac >= limit:
        print("It is not legal for you to drive.")
    else:
        print("It is legal for you to drive.")

### MAIN ###

if __name__ == '__main__':
    main()

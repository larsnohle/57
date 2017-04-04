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


def calculate_bmi(weight, height):
    return (weight / (height * height)) * 703

def main():
    weight = get_positive_number_input("Please enter your weight: ")
    height = get_positive_number_input("Please enter your height: ")

    bmi = calculate_bmi(weight, height)

    if (bmi < 18.5):
        print("You are underweight. You should see your doctor.")
    elif (bmi > 28.5):
        print("You are overweight. You should see your doctor.")
    else:
        print("You are within the ideal weight range.")

### MAIN ###

if __name__ == '__main__':
    main()


###################################################################



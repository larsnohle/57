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

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s


def calculate_bmi_using_imperial_units(weight, height):
    return (weight / (height * height)) * 703

def calculate_bmi_using_metric_units(weight, height):
    return weight / (height * height)


def main():
    weight = get_positive_number_input("Please enter your weight: ", True)
    height = get_positive_number_input("Please enter your height: ", True)
    unit = get_string_input("Metric (m) or imperial (i) units? ", ["M", "m", "I", "i"])

    if unit == "I" or unit == "i":
        bmi = calculate_bmi_using_imperial_units(weight, height)
    else:
        bmi = calculate_bmi_using_metric_units(weight, height)

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



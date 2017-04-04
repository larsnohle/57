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

def input_scale():
    done = False
    print("Press C to convert from Fahrenheit to Celsius.")
    print("Press F to convert from Celsius to Fahrenheit.")
    while not done:
        scale = input("Your choice? ")
        if scale == 'C' or scale == 'c' or scale == 'F' or scale == 'f':
            scale = scale.upper()
            done = True
    return scale

def input_and_convert_from_celsius():
    c = get_positive_number_input("Please enter the temperature in Celsius: ")
    f = (c * 9.0 / 5.0) + 32
    print("The temperature in Fahrenheit is %.1f" % f)

def input_and_convert_from_fahrenheit():
    f = get_positive_number_input("Please enter the temperature in Fahrenheit: ")
    c = (f - 32) * 5.0 / 9.0
    print("The temperature in Celsius is %.1f" % c)

def main():
    scale = input_scale()
    if scale == "C":
        input_and_convert_from_celsius()
    else:
        input_and_convert_from_fahrenheit()    

### MAIN ###

if __name__ == '__main__':
    main()


###################################################################



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

def main():
    month_as_number = get_positive_number_input("Please enter the number of the month: ")
    string_to_output = "The name of the month is "

    if month_as_number == 1:
        string_to_output += "Januari"
    elif month_as_number == 2:
        string_to_output += "February"
    elif month_as_number == 3:
        string_to_output += "March"
    elif month_as_number == 4:
        string_to_output += "April"
    elif month_as_number == 5:
        string_to_output += "May"
    elif month_as_number == 6:
        string_to_output += "June"
    elif month_as_number == 7:
        string_to_output += "July"
    elif month_as_number == 8:
        string_to_output += "August"
    elif month_as_number == 9:
        string_to_output += "September"
    elif month_as_number == 10:
        string_to_output += "October"
    elif month_as_number == 11:
        string_to_output += "November"
    elif month_as_number == 12:
        string_to_output += "December"
    else:
        string_to_output += "there is no such month!"

    string_to_output += "."

    print(string_to_output)

### MAIN ###

if __name__ == '__main__':
    main()



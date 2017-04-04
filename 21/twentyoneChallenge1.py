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
    month_dict = {}
    month_dict[1] = "Januari"
    month_dict[2] = "February"
    month_dict[3] = "March"
    month_dict[4] = "April"
    month_dict[5] = "May"
    month_dict[6] = "June"
    month_dict[7] = "July"
    month_dict[8] = "August"
    month_dict[9] = "September"
    month_dict[10] = "October"
    month_dict[11] = "November"
    month_dict[12] = "December"

    month_as_string = month_dict.get(month_as_number, "there is no such month!")

    string_to_output = "The name of the month is %s." % month_as_string 

    print(string_to_output)

### MAIN ###

if __name__ == '__main__':
    main()



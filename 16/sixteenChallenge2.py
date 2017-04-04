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
    country_to_age = dict()
    country_to_age["US"] = 16
    country_to_age["SE"] = 18
    country_to_age["NO"] = 18

    age = get_positive_number_input("What is your age? ")

    for (country, age_in_country) in country_to_age.items():
        if age >= age_in_country:
            print(country)

### MAIN ###

if __name__ == '__main__':
    main()

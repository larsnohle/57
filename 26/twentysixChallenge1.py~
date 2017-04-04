#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

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


def calculateMonthsUntilPaidOff(balance, apr_as_percentage, monthly_payment):
    apr = apr_as_percentage / 100.0
    i = apr / 365.0 
    nominator_before_log = 1 + balance * (1 - math.pow(1 + i, 30))/ monthly_payment
    nominator = math.log10(nominator_before_log)
    denominator = 30 * math.log10(1 + i)
    return -math.ceil(nominator / denominator)

def main():
    balance = get_positive_number_input("What is your balance? ")
    apr_as_percentage = get_positive_number_input("What is the APR on the card (as a percent)? ", True)
    monthly_payment = get_positive_number_input("What is the monthly payment you can make? ")

    number_of_months = calculateMonthsUntilPaidOff(balance, apr_as_percentage, monthly_payment)
    print("It will take you %d months to pay off this card." % number_of_months)

### MAIN ###

if __name__ == '__main__':
    main()



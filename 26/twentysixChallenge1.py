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

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def calculateMonthsUntilPaidOff(balance, apr_as_percentage, monthly_payment):
    apr = apr_as_percentage / 100.0
    i = apr / 365.0 
    nominator_before_log = 1 + balance * (1 - math.pow(1 + i, 30))/ monthly_payment
    nominator = math.log10(nominator_before_log)
    denominator = 30 * math.log10(1 + i)
    return -math.ceil(nominator / denominator)

def calculate_number_of_months():
    balance = get_positive_number_input("What is your balance? ")
    apr_as_percentage = get_positive_number_input("What is the APR on the card (as a percent)? ", True)
    monthly_payment = get_positive_number_input("What is the monthly payment you can make? ")

    number_of_months = calculateMonthsUntilPaidOff(balance, apr_as_percentage, monthly_payment)
    print("It will take you %d months to pay off this card." % number_of_months)

def calculate_monthly_payment(balance, apr_as_percentage, number_of_months):
    apr = apr_as_percentage / 100.0
    i = apr / 365.0 
    denominator = math.pow(30 * math.log10(1 + i), 10) - 1
    nominator = balance * (1 - math.pow(1 + i, 30))
    return nominator / denominator

def calculate_amount_per_month():
    balance = get_positive_number_input("What is your balance? ")
    apr_as_percentage = get_positive_number_input("What is the APR on the card (as a percent)? ", True)
    number_of_months = get_positive_number_input("How many months? ")

    amount_per_month = calculate_monthly_payment(balance, apr_as_percentage, number_of_months)
    print("Amount per month %.2f" % amount_per_month)


def main():
    choice = get_string_input("Number of months (m) or amount per month(a)? ", ['m', 'a'])

    if choice == 'm':
        calculate_number_of_months()
    elif choice == 'a':
        calculate_amount_per_month()
    else:
        print("Incorrect choice!") # Should not happen.

### MAIN ###

if __name__ == '__main__':
    main()



#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def round_cents_up(amount):
    numberOfWholeDollars = math.trunc(amount)
    numberOfPennies = math.ceil((amount - numberOfWholeDollars) * 100)    
    adjustedAmount = numberOfWholeDollars + numberOfPennies / 100
    return adjustedAmount

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
    order_amount = get_positive_number_input("What is the order amount? ", True)
    state = input("What is the state? ")
    total = order_amount

    # Set up dict containing tax rates for the counties in WI.
    wisconsin_tax_dict = {}
    wisconsin_tax_dict['EAU CLAIRE'] = 0.055 + 0.005
    wisconsin_tax_dict['DUNNE'] = 0.055 + 0.004

    # Determine tax.
    tax = 0
    string_to_output = ""
    state = state.upper()
    if state == "WI" or state == 'WISCONSIN':
        wi_default_tax = 0.055
        county = input("What is the county? ")
        county = county.upper()
        tax = wisconsin_tax_dict.get(county, wi_default_tax)
    elif state == "IL" or state == 'Illinois':
        tax = 0.08
    elif state == "SWE" or state == 'SVERIGE':
        tax = 0.25

    total = order_amount
    if tax > 0:
        string_to_output += "The subtotal is $%.2f.\n" % order_amount
        tax_amount = round_cents_up(order_amount * tax)
        string_to_output += "The tax is $%.2f\n" % tax_amount
        total += tax_amount

    string_to_output += "The total is $%.2f." % total
    print(string_to_output)

### MAIN ###

if __name__ == '__main__':
    main()

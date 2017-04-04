import math

### Functions
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

### MAIN

principal = get_positive_number_input("Enter the principal: ")
rate =  get_positive_number_input("Enter the rate of interest: ", True) / 100.0
number_of_years = get_positive_number_input("Enter the number of years: ")

final_amount = principal * (1 + rate) ** number_of_years

number_of_whole_dollars = math.trunc(final_amount)
number_of_pennies = math.ceil((final_amount - number_of_whole_dollars) * 100)

adjusted_amount = number_of_whole_dollars + number_of_pennies / 100

print("After %d years at %s percent, the investment will be worth $%.2f." % (number_of_years, str(rate), adjusted_amount))


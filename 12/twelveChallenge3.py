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

def calculateSimpleInterest(principal, rate, number_of_years):
    year = 1
    tmp_amount = principal
    while year <= number_of_years:
        tmp_amount *= (1 + rate)
        print("Amount year %d is %.2f" % (year, tmp_amount))
        year += 1
    
    final_amount = tmp_amount
    number_of_whole_dollars = math.trunc(final_amount)
    number_of_pennies = math.ceil((final_amount - number_of_whole_dollars) * 100)
    adjusted_amount = number_of_whole_dollars + number_of_pennies / 100
    return adjusted_amount


### MAIN

principal = get_positive_number_input("Enter the principal: ")
rate =  get_positive_number_input("Enter the rate of interest: ", True) / 100.0
number_of_years = get_positive_number_input("Enter the number of years: ")

adjusted_amount = calculateSimpleInterest(principal, rate, number_of_years)
print("After %d years at %s percent, the investment will be worth $%.2f." % (number_of_years, str(rate * 100), adjusted_amount))


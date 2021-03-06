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

# What is the principal amount? 1500
# What is the rate? 4.3
# What is the number of years? 6
# What is the number of times the interest is compounded per year? 4
# $1500 invested at 4.3% for 6 years compounded 4 times per year is $1938.84.

target_amount = get_positive_number_input("What is the target amount: ")

#principal = get_positive_number_input("Enter the principal: ")
rate =  get_positive_number_input("Enter the rate of interest: ", True) / 100.0
number_of_years = get_positive_number_input("Enter the number of years: ")
number_of_compounds_per_year = get_positive_number_input("What is the number of times the interest is compounded per year? ")

principal =  target_amount / (1 + rate / number_of_compounds_per_year) ** (number_of_years * number_of_compounds_per_year)

# Round cents upwards to the nearest whole cent.
number_of_whole_dollars = math.trunc(principal)
number_of_pennies = math.ceil((principal - number_of_whole_dollars) * 100)

adjusted_amount = number_of_whole_dollars + number_of_pennies / 100

print("You need to invest $%.2f to have %d after %d years at %s percent." % (adjusted_amount, target_amount, number_of_years, str(rate * 100)))


import math

# What is the principal amount? 1500
# What is the rate? 4.3
# What is the number of years? 6
# What is the number of times the interest is compounded per year? 4
# $1500 invested at 4.3% for 6 years compounded 4 times per year is $1938.84.

principal_string = input("Enter the principal: ")
rate_string = input("Enter the rate of interest: ")
number_of_years_string = input("Enter the number of years: ")
number_of_compounds_per_year_string = input("What is the number of times the interest is compounded per year? ")


principal = int(principal_string)
rate = float(rate_string) / 100.0
number_of_years = int(number_of_years_string) 
number_of_compounds_per_year = int(number_of_compounds_per_year_string)

final_amount = principal * (1 + rate / number_of_compounds_per_year) ** (number_of_years * number_of_compounds_per_year)

number_of_whole_dollars = math.trunc(final_amount)
number_of_pennies = math.ceil((final_amount - number_of_whole_dollars) * 100)

adjusted_amount = number_of_whole_dollars + number_of_pennies / 100

print("After %d years at %s percent, the investment will be worth $%.2f." % (number_of_years, rate_string, final_amount))


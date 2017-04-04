import math

#Enter the principal: 1500
#Enter the rate of interest: 4.3
#Enter the number of years: 4
#After 4 years at 4.3%, the investment will
#be worth $1758.

principal_string = input("Enter the principal: ")
rate_string = input("Enter the rate of interest: ")
number_of_years_string = input("Enter the number of years: ")

principal = int(principal_string)
rate = float(rate_string) / 100.0
number_of_years = int(number_of_years_string) 

final_amount = principal * (1 + rate) ** number_of_years

number_of_whole_dollars = math.trunc(final_amount)
number_of_pennies = math.ceil((final_amount - number_of_whole_dollars) * 100)

adjusted_amount = number_of_whole_dollars + number_of_pennies / 100

print("After %d years at %s percent, the investment will be worth $%.2f." % (number_of_years, rate_string, final_amount))


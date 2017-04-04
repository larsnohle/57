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

def get_rate_from_dict(exchange_rate_dict):
    done = False
    rate = None
    while not done:
        country = input("What country's currency are you exchanging? ")
        if country in exchange_rate_dict:
            rate = exchange_rate_dict[country]
            done = True
        else:
            print("Sorry, don't have any exchange rate for %s " % country)
        
    return rate

conversion_dict = {}
conversion_dict["EU"] = 137.51
conversion_dict["SE"] = 15.28

# Get input.
number_of_euros = get_positive_number_input("What amount of money are you exchanging? ")

exchange_rate = get_rate_from_dict(conversion_dict)

# Perform calculations.
number_of_cents = number_of_euros * exchange_rate
number_of_cents_rounded = math.ceil(number_of_cents)
number_of_dollars = number_of_cents_rounded  / 100.0

# Print output.
print("%d euros at an exchange rate of %.2f is %.2f U.S. dollars." % (number_of_euros, exchange_rate, number_of_dollars))



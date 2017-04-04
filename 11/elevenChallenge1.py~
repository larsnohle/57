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


# Get input.
number_of_euros = get_positive_number_input("How many euros are you exchanging? ")
exchange_rate = get_positive_number_input("What is the exchange rate? ", True)

# Perform calculations.
number_of_cents = number_of_euros * exchange_rate
number_of_cents_rounded = math.ceil(number_of_cents)
number_of_dollars = number_of_cents_rounded  / 100.0

# Print output.
print("%d euros at an exchange rate of %.2f is %.2f U.S. dollars." % (number_of_euros, exchange_rate, number_of_dollars))



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

    string_to_output = ""
    state = state.upper()
    if state == "WI" or state == 'WISCONSIN':
        string_to_output += "The subtotal is $%.2f.\n" % order_amount
        tax = round_cents_up(order_amount * 0.055)
        string_to_output += "The tax is $%.2f\n" % tax
        total += tax

    string_to_output += "The total is $%.2f." % total
    print(string_to_output)

### MAIN ###

if __name__ == '__main__':
    main()

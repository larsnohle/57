def get_positive_integer_input(msg):
    done = False
    while not done:
        try:
            i = int(input(msg))
            if i < 0:
                print("Please enter a number > 0")
            else:
                done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")

    return i


price_1    = get_positive_integer_input("Enter the price of item 1: ")
quantity_1 = get_positive_integer_input("Enter the price of item 1: ")
price_2    = get_positive_integer_input("Enter the price of item 2: ")
quantity_2 = get_positive_integer_input("Enter the price of item 2: ")
price_3    = get_positive_integer_input("Enter the price of item 3: ")
quantity_3 = get_positive_integer_input("Enter the price of item 3: ")

subtotal = price_1 * quantity_1 + price_2 * quantity_2 + price_3 * quantity_3
tax = subtotal * 0.055
total = subtotal + tax

print("Subtotal: $%.2f" % subtotal)
print("Tax: $%.2f" % tax)
print("Total: $%.2f" % total)

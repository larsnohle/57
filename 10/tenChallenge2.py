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


# MAIN
done = False
counter = 1
price_quantity_list = list()
while not done:
    try:
        price    = get_positive_integer_input("Enter the price of item %d: " % counter)
        quantity = get_positive_integer_input("Enter the price of item %d: " % counter)
        counter +=1
        price_quantity_list.append((price, quantity))
        
    except EOFError:
        done = True

# The calculation could also be made inside the loop where the prices and quantities are added, but I like it better this way ;)
subtotal = 0
for (price, quantity) in price_quantity_list:
    subtotal += price * quantity

tax = subtotal * 0.055
total = subtotal + tax

print("\nSubtotal: $%.2f" % subtotal)
print("Tax: $%.2f" % tax)
print("Total: $%.2f" % total)

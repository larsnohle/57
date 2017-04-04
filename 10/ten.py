price_1_string    = input("Enter the price of item 1: ")
quantity_1_string = input("Enter the price of item 1: ")
price_2_string    = input("Enter the price of item 2: ")
quantity_2_string = input("Enter the price of item 2: ")
price_3_string    = input("Enter the price of item 3: ")
quantity_3_string = input("Enter the price of item 3: ")

price_1 = int(price_1_string)
quantity_1 = int(quantity_1_string)
price_2  = int(price_2_string)
quantity_2 = int(quantity_2_string)
price_3  = int(price_3_string)
quantity_3 = int(quantity_3_string)

subtotal = price_1 * quantity_1 + price_2 * quantity_2 + price_3 * quantity_3
tax = subtotal * 0.055
total = subtotal + tax

print("Subtotal: $%.2f" % subtotal)
print("Tax: $%.2f" % tax)
print("Total: $%.2f" % total)

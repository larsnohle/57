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


width_1 = get_positive_integer_input("Width 1? ")
length_1 = get_positive_integer_input("Length 1? ")

width_2 = get_positive_integer_input("Width 2? ")
length_2 = get_positive_integer_input("Length 2? ")

area = width_1 * length_1 + width_2 * length_2 - width_2 * length_1 

gallons_of_paint_needed = area / 350
if area % 350 != 0:
    gallons_of_paint_needed += 1

print("You will need to purchase %d gallons of paint to cover %d square feet." % (gallons_of_paint_needed, area))

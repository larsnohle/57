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

feet2_to_m2_conversion_factor = 0.09290304

length_in_feet = get_positive_integer_input("What is the length of the room in feet? ")
width_in_feet = get_positive_integer_input("What is the width of the room in feet? ")

area_in_feet = length_in_feet * width_in_feet
area_in_m = area_in_feet * feet2_to_m2_conversion_factor

print("You entered dimensions of %d feet by %d feet." % (length_in_feet, width_in_feet))
print("The area is:")
print("%d square feet." % area_in_feet)
print("%f square meter." % area_in_m)

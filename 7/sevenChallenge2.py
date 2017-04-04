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

def let_user_select_m_or_feet():
    done = False
    while not done:
        selection = input("Select m or f: ")
        if selection == 'm' or selection == 'f':
            done = True 

    return selection


feet2_to_m2_conversion_factor = 0.09290304
m2_to_feet2_conversion_factor = 1.0 / 0.09290304

m_or_f = let_user_select_m_or_feet()

if m_or_f == 'f':
    length_in_feet = get_positive_integer_input("What is the length of the room in feet? ")
    width_in_feet = get_positive_integer_input("What is the width of the room in feet? ")
    area_in_feet = length_in_feet * width_in_feet
    area_in_m = area_in_feet * feet2_to_m2_conversion_factor
    first_output_line = "You entered dimensions of %d feet by %d feet." % (length_in_feet, width_in_feet)
else:
    length_in_m = get_positive_integer_input("What is the length of the room in m? ")
    width_in_m = get_positive_integer_input("What is the width of the room in m? ")
    area_in_m = length_in_m * width_in_m
    area_in_feet = area_in_m * m2_to_feet2_conversion_factor
    first_output_line = "You entered dimensions of %d m by %d m." % (length_in_m, width_in_m)

print(first_output_line)
print("The area is:")
print("%.2f square feet." % area_in_feet)
print("%.2f square meter." % area_in_m)

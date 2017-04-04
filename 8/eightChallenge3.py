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


number_of_people = get_positive_integer_input("How many people? ")
number_of_pieces_per_pizza = get_positive_integer_input("How many pieces per pizza? ")
number_of_pieces_per_person = get_positive_integer_input("How many pieces do each person want? ")

desired_number_of_slices = number_of_people * number_of_pieces_per_person
number_of_pizzas_needed = desired_number_of_slices / number_of_pieces_per_pizza

if desired_number_of_slices % number_of_pieces_per_pizza != 0:
    number_of_pizzas_needed += 1

print("%d number of pizzas are needed" % number_of_pizzas_needed)

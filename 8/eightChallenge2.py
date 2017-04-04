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


number_of_people_string = input("How many people? ")
number_of_pizzas_string = input("How many pizzas do you have? ")
number_of_slices_per_pizza = input("How many slices per pizza? ")

number_of_people = int(number_of_people_string)
number_of_pizzas = int(number_of_pizzas_string)
number_of_slices_per_pizza = int(number_of_slices_per_pizza)

total_number_of_pizza_slices = number_of_pizzas * number_of_slices_per_pizza
number_of_slices_per_person = total_number_of_pizza_slices / number_of_people
number_of_leftover_slices = total_number_of_pizza_slices % number_of_people

if number_of_slices_per_person == 1:
    piece_or_pieces_string_per_person = "piece"
else:
    piece_or_pieces_string_per_person = "pieces"

if number_of_leftover_slices == 1:
    piece_or_pieces_string_leftover = "piece"
else:
    piece_or_pieces_string_leftover = "pieces"


print("%d people with %d pizzas." % (number_of_people, number_of_pizzas))
print("Each person gets %d %s of pizza." % (number_of_slices_per_person, piece_or_pieces_string_per_person))
print("There are %d leftover %s." % (number_of_leftover_slices, piece_or_pieces_string_leftover))

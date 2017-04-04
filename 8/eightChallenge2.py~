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

print("%d people with %d pizzas." % (number_of_people, number_of_pizzas))
print("Each person gets %d pieces of pizza." % number_of_slices_per_person)
print("There are %d leftover pieces." % number_of_leftover_slices)

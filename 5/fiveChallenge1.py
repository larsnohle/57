# Displayes the specified message in an input() statement and validates that the specified string can be translated to an integer. If it cannot, the message is repeaded again until a valid integer, which then is returned, is entered.
def get_integer_input(msg):
    done = False
    while not done:
        try:
            i = int(input(msg))
            done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")

    return i

i1 = get_integer_input("What is the first number? ")
i2 = get_integer_input("What is the second number? ")

string_to_output = "%d + %d = %d\n%d - %d = %d\n%d * %d = %d\n%d / %d = %d" % (i1, i2, i1 + i2, i1, i2, i1 - i2, i1, i2, i1 * i2, i1, i2, i1 / i2)
print(string_to_output)



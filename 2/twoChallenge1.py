done = False
while not done:
    input_string = input("What's the input string? ")
    if len(input_string) > 0:
        output_string = "%s has %d characters." % (input_string, len(input_string))
        print(output_string)
        done = True
    else:
        print("Please enter a string!")

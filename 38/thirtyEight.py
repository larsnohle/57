#!/usr/bin/python3
# -*- coding: utf-8 -*-

def get_ints_from_user():
    ints_to_return = list()
    input_row = input("Enter a list of numbers, separated by spaces: ")
    for s in input_row.split(" "):
        if s.strip() != "":
            try:
                i = int(s)
                ints_to_return.append(i)
            except:
                print("%s is not an integer!" % s)
    return ints_to_return

def filter_even_numbers(list_of_ints):
    even_ints = list()
    for i in list_of_ints:
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints

def print_output(list_of_ints):
    string_of_ints = ' '.join([str(x) for x in list_of_ints])
    print("The even numbers are: %s" % string_of_ints)


def main():
    print_output(filter_even_numbers(get_ints_from_user()))
    
### MAIN ###

if __name__ == '__main__':
    main()

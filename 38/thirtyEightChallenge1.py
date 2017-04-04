#!/usr/bin/python3
# -*- coding: utf-8 -*-

FILENAME = "input.txt"

def get_ints_from_file(filename):
    ints_to_return = list()
    f = open(filename, 'r')
    for row in f:
        for s in row.split(" "):
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
    print_output(filter_even_numbers(get_ints_from_file(FILENAME)))
    
### MAIN ###

if __name__ == '__main__':
    main()

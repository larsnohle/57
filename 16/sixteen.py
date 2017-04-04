#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    age_string = input("What is your age? ")
    age = int(age_string)

    output_string = "You are old enough to legally drive." if age >= 16 else "You are not old enough to legally drive."

    print(output_string)

### MAIN ###

if __name__ == '__main__':
    main()

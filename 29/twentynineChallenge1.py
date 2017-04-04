#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    done = False
    while not done:
        try:
            s = input("What is the rate of return? ")
            rate = int(s)
            if rate > 0:
                rate = int(s)
                years = 72 / rate
                print("t will take %d years to double your initial investment." % years)
                done = True
            else:
                print("Sorry. Zero is not a valid input.")
        except ValueError:
            print("Sorry. That's not a valid input.")        


### MAIN ###

if __name__ == '__main__':
    main()



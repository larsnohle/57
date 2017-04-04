#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    sum = 0
    for i in range(0, 5):
        num = int(input("Enter a number: "))
        sum += num

    print("The total is %d." % sum) 

### MAIN ###

if __name__ == '__main__':
    main()



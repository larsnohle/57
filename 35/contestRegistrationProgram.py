#!/usr/bin/python3
# -*- coding: utf-8 -*-

FILENAME = "contestants.txt"

def write_to_file(s):
    f = open(FILENAME, 'a')
    f.write(s)
    
def main():
    done = False
    contestants = list()
    while not done:
        try:
            contestant = input("Enter a name: ")
            write_to_file(contestant + "\n")
        except EOFError:
            done = True
                        
### MAIN ###

if __name__ == '__main__':
    main()




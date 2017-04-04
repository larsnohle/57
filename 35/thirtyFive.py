#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

def main():
    done = False
    contestants = list()
    while not done:
        try:
            contestant = input("Enter a name: ")
            contestants.append(contestant)
        except EOFError:
            done = True

    winner_index = random.randint(0, len(contestants) - 1)
    print("And the winner is....%s " % contestants[winner_index])
            
        
### MAIN ###

if __name__ == '__main__':
    main()




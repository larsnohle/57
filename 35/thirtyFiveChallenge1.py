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

    winner_ordinal = 1
    print("")
    while len(contestants) > 0:
        winner_index = random.randint(0, len(contestants) - 1)
        winner = contestants.pop(winner_index)
        print("And the winner number %d is....%s " % (winner_ordinal, winner))
        winner_ordinal += 1
            
        
### MAIN ###

if __name__ == '__main__':
    main()




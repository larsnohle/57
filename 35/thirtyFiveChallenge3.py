#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

FILENAME = "contestants.txt"

def read_contestants():
    f = open(FILENAME, 'r')
    contestants = list()
    for contestant in f:
        contestants.append(contestant.strip())

    return contestants
        

def main():
    done = False
    contestants = read_contestants()

    winner_index = random.randint(0, len(contestants) - 1)
    winner = contestants.pop(winner_index)
    print("And the winner number is....%s " % winner)
            
        
### MAIN ###

if __name__ == '__main__':
    main()




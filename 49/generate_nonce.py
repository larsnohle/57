#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

lower_case_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
upper_case_letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sequences_to_pick_data_from = [lower_case_letters, upper_case_letters, digits]

def generate_random_string(length):
    l = list()
    for i in range(length):
        sequence = sequences_to_pick_data_from[random.randint(0, len(sequences_to_pick_data_from) - 1)]
        c = sequence[random.randint(0, len(sequence) - 1)]
        l.append(c)
    return ''.join(l)

def main():
    print(generate_random_string(32))

### MAIN ###

if __name__ == '__main__':
    main()

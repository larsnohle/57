#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

ANSWERS = ["Yes", "No", "Maybe", "Ask again later."]

def main():
    question = input("What's your question? ")
    answer_index = random.randint(0, len(ANSWERS) - 1)
    print(ANSWERS[answer_index])
        
### MAIN ###

if __name__ == '__main__':
    main()




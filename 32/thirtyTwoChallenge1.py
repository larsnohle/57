#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

def create_result_message(number_of_guesses):
    if number_of_guesses == 1:
        s = "You’re a mind reader!"
    elif number_of_guesses >= 2 and number_of_guesses <= 4:
        s = "Most impressive."
    elif number_of_guesses >= 5 and number_of_guesses <= 6:
        s = "You can do better than that."
    else:
        s = "Better luck next time"
    return s
        
def get_positive_number_input(msg, to_float = False):
    done = False
    number_of_bad_inputs = 0
    while not done:
        try:
            i = -1.0
            if to_float == True:
                i = float(input(msg))
            else:
                i = int(input(msg))
            if i < 0:
                print("Please enter a number > 0")
            else:
                done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")
            number_of_bad_inputs += 1

    return (i, number_of_bad_inputs) 

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s


def play_round():
    print("Let's play Guess the Number.")
    inputted_difficulty_level = get_string_input("Pick a difficulty level (1, 2, or 3): ", ["1", "2", "3"])

    end_number = 10
    if inputted_difficulty_level == 2:
        end_number = 100
    elif inputted_difficulty_level == 3:
        end_number = 100

    goal_number = random.randint(1, end_number)
    (answer, number_of_bad_inputs)  = get_positive_number_input(    "I have my number. What's your guess?")
    number_of_tries = 1 + number_of_bad_inputs
    while answer != goal_number:
        if answer < goal_number:
            msg = "Too low. Guess again:"
        else:
            msg = "Too high. Guess again:"
            
        (answer, number_of_bad_inputs) = get_positive_number_input(msg)
        number_of_tries += 1
        number_of_tries += number_of_bad_inputs
        
    print("You got it in %d guesses!" % number_of_tries)
    print(create_result_message(number_of_tries))

def main():
    play_round()
    should_play_again = get_string_input("Play again (y, n)? ", ["y", "Y", "n", "N"])
    while should_play_again == "y" or should_play_again == "Y":
        play_round()
        should_play_again = get_string_input("Play again (y, n)? ", ["y", "Y", "n", "N"])
        
    print("Goodbye!")

        
### MAIN ###

if __name__ == '__main__':
    main()




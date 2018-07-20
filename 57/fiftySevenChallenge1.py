#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import random

# CONSTANTS
QUESTIONS = "questions"
QUESTION = "question"
ANSWER = "answer"
DISTRACTORS = "distractors"
LEVEL = 'level'

FILENAME = "triviaChallenge1.json"

def check_items_exist_up_to_index(l, index):
    current_len = len(l)
    if current_len > index:
        return
    current_largest_index = current_len - 1
    while current_largest_index < index:
        l.append(list())
        current_largest_index += 1

def group_trivia_questions(trivia_dict):
    trivia_questions_unsorted = list()
    trivia_questions_grouped = list()
    for trivia_question in trivia_dict[QUESTIONS]:
        level = trivia_question[LEVEL]
        check_items_exist_up_to_index(trivia_questions_grouped, level - 1)
        trivia_questions_grouped[level - 1].append(trivia_question)
    return trivia_questions_grouped

    
def initialize_questions_dict():
    with open(FILENAME, 'r') as f:        
        trivia_dict = json.load(f)
    return trivia_dict

# Get input from user. Only allow certain responses.
def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def generate_alternatives(question_item):
    l = list()
    l.append(question_item[ANSWER])
    for distractor in question_item[DISTRACTORS]:
        l.append(distractor)
    alternatives = list()
    while len(l) > 0:
        alternatives.append(l.pop(random.randint(0, len(l) - 1)))
    return alternatives
        
def display_random_question(trivia_questions):
    question_item = trivia_questions.pop(random.randint(0, len(trivia_questions) - 1))
    alternatives = generate_alternatives(question_item)
    allowed_responses = [str(i) for i in range(1, len(alternatives) + 1)]

    print("\nQuestion: %s" % question_item[QUESTION])
    for (i, alternative) in enumerate(alternatives):
        print("%d) %s" % (i + 1, alternative))
    choice = get_string_input("Your choice: ", allowed_responses)

    answer = alternatives[int(choice) - 1]
    if answer == question_item[ANSWER]:
        print("That was correct!")
        return True
    else:
        print("That was wrong!")
        return False
    
def main():
    trivia_dict = initialize_questions_dict()
    trivia_questions_grouped = group_trivia_questions(trivia_dict)

    game_finished = False
    number_of_correct_answers = 0
    level = 1
    while not game_finished and level <= len(trivia_questions_grouped):
        user_answered_correctly = display_random_question(trivia_questions_grouped[level - 1])
        if not user_answered_correctly:
            print("Game over. You lost.")
            print("You had %d number of correct answers" % number_of_correct_answers)
            game_finished = True            
        else:
            number_of_correct_answers += 1            
            if level == 5:
                print("Game over. You won!")
                print("You had %d correct answers" % number_of_correct_answers)
                game_finished = True
            else:
                level += 1

### MAIN ###

if __name__ == '__main__':
    main()

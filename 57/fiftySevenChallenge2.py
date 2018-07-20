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

FILENAME = "triviaChallenge2.json"

PLAY_GAME_CHOICE = '1'
ADD_QUESTION_CHOICE = '2'
EDIT_QUESTION_CHOICE = '3'
REMOVE_QUESTION_CHOICE = '4'
DISPLAY_QUESTIONS_CHOICE = '5'
QUIT_CHOICE = 'q'
ALLOWED_RESPONSES= [PLAY_GAME_CHOICE, ADD_QUESTION_CHOICE, EDIT_QUESTION_CHOICE, REMOVE_QUESTION_CHOICE, QUIT_CHOICE, DISPLAY_QUESTIONS_CHOICE]

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

def get_non_empty_string_input(msg):
    done = False
    s = ""
    while not done:
        s = input(msg)
        s = s.strip()
        if len(s) > 0:
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
    
def play_game():
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

def add_question():
    question = get_non_empty_string_input("Question: ")
    answer = get_non_empty_string_input("Answer: ")
    distractor_1      = get_non_empty_string_input("Distractor 1: ")
    distractor_2      = get_non_empty_string_input("Distractor 2: ")
    distractor_3      = get_non_empty_string_input("Distractor 3: ")
    level = int(get_string_input('Level: ', ['1','2','3','4','5']))
    new_question_dict = {QUESTION: question, ANSWER: answer, DISTRACTORS: [distractor_1, distractor_2, distractor_3], LEVEL: level}

    trivia_dict = initialize_questions_dict()
    trivia_dict[QUESTIONS].append(new_question_dict)
    save_trivia_dict(trivia_dict)
    print("Question saved!")

def save_trivia_dict(trivia_dict):
    with open(FILENAME, 'w') as f:
        json.dump(trivia_dict, f)
    
def display_questions(questions):
    for (index, question) in enumerate(questions):
        print("%d) %s" % (index + 1, question[QUESTION]))    
    
def remove_question():
    trivia_dict = initialize_questions_dict()
    questions = trivia_dict[QUESTIONS]
    display_questions(questions)
    allowed_responses = [str(i) for i in range(1, len(questions) + 1)]
    choice = get_string_input("Enter the number of the question to remove:  ", allowed_responses)
    sure = get_string_input("Are you sure you want to remove the question[yYnN]:  ", ['y','Y','n','N'])
    if sure == 'y' or sure == 'Y':
        index_to_remove = int(choice) - 1
        questions.pop(index_to_remove)
        save_trivia_dict(trivia_dict)
        print("Question removed!")
    
def edit_question():
    trivia_dict = initialize_questions_dict()
    questions = trivia_dict[QUESTIONS]
    display_questions(questions)
    allowed_responses = [str(i) for i in range(1, len(questions) + 1)]
    choice = get_string_input("Enter the number of the question to edit:  ", allowed_responses)
    index_of_question_to_edit = int(choice) - 1

    question_to_edit = questions[index_of_question_to_edit]
    print("Old question text: %s" % question_to_edit[QUESTION])
    new_question_text = get_non_empty_string_input("Please enter a new question text: ")
    print("Old answer: %s" % question_to_edit[ANSWER])
    new_answer = get_non_empty_string_input("Please enter a new answer: ")
    new_distractors = list()
    for (distractor_index, distractor) in enumerate(question_to_edit[DISTRACTORS]):
        print("Old distractor %d: %s" % (distractor_index, distractor))
        new_disractor = get_non_empty_string_input("Please enter a new disractor %d: " % distractor_index)
        new_distractors.append(new_disractor)
    print("Old level: %d" % question_to_edit[LEVEL])
    new_level = int(get_string_input('Plese enter a new level: ', ['1','2','3','4','5']))

    question_to_edit[QUESTION] = new_question_text
    question_to_edit[ANSWER] = new_answer
    question_to_edit[DISTRACTORS] = new_distractors
    question_to_edit[LEVEL] = new_level
    save_trivia_dict(trivia_dict)
    
def display_main_menu():
    print("*************************")
    print("*       MAIN MENU       *")
    print("*************************")
    print("1) Play game.")
    print("2) Add question.")
    print("3) Edit question")
    print("4) Remove question")
    print("5) Display questions")
    print("q) Quit")
        

def main():
    done = False
    while not done:
        display_main_menu()
        choice = get_string_input('Choice: ', ALLOWED_RESPONSES)
        if choice == QUIT_CHOICE:
            done = True
        elif choice == PLAY_GAME_CHOICE:
            items_dict = play_game()
        elif choice == ADD_QUESTION_CHOICE:
            add_question()
        elif choice == EDIT_QUESTION_CHOICE:
            edit_question()
        elif choice == DISPLAY_QUESTIONS_CHOICE:
            trivia_dict = initialize_questions_dict()
            questions = trivia_dict[QUESTIONS]
            display_questions(questions)
        elif choice == REMOVE_QUESTION_CHOICE:
            remove_question()
            pass
                
### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
#import os.listdir
#import os.path

IN_FILE_NAME = 'inputFile.txt'
REPLACEMENT_WORDS_FILE_NAME = 'replacementWords.csv'
PLEASE_ENTER_DIR = 'Please enter name of directory to process: '
COMMA = ','

def get_string_input(msg):
    done = False
    s = ""
    while not done:
        s = input(msg)
        s = s.strip()
        if len(s) > 0:
            done = True
    return s


def read_replacement_file():
    replacement_dictionary = dict()
    with open(REPLACEMENT_WORDS_FILE_NAME, 'r') as f:
        for line in f:
            (word_to_replace, replacement_word) = line.split(COMMA)
            replacement_dictionary[word_to_replace] = replacement_word.strip()
    return replacement_dictionary

def replace_words_and_write_to_file(input_file_name, output_file_name, replacement_dictionary):
    number_of_replacements = 0
    with open(input_file_name, 'r') as infile, open(output_file_name, 'w') as outfile:
        for line in infile:
            for (word_to_replace, replacement_word) in replacement_dictionary.items():
                while word_to_replace in line:
                    line = line.replace(word_to_replace, replacement_word, 1)
                    number_of_replacements += 1
            outfile.write(line)
    print("Number of replacements done: %d" % number_of_replacements)
    

def main():
    replacement_dictionary = read_replacement_file()
    directory_name = get_string_input(PLEASE_ENTER_DIR)

    for f in os.listdir(directory_name):
        name_of_possible_input_file = os.path.join(directory_name, f)
        if os.path.isfile(name_of_possible_input_file):
            output_file_name = name_of_possible_input_file + '_modified'
            replace_words_and_write_to_file(name_of_possible_input_file, output_file_name, replacement_dictionary)
        
### MAIN ###

if __name__ == '__main__':
    main()

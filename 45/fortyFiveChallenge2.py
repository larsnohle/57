#!/usr/bin/python3
# -*- coding: utf-8 -*-

IN_FILE_NAME = 'inputFile.txt'
REPLACEMENT_WORDS_FILE_NAME = 'replacementWords.csv'
COMMA = ','

def read_replacement_file():
    replacement_dictionary = dict()
    with open(REPLACEMENT_WORDS_FILE_NAME, 'r') as f:
        for line in f:
            (word_to_replace, replacement_word) = line.split(COMMA)
            replacement_dictionary[word_to_replace] = replacement_word.strip()
    return replacement_dictionary

def replace_words_and_write_to_file(output_file_name, replacement_dictionary):
    number_of_replacements = 0
    with open(IN_FILE_NAME, 'r') as infile, open(output_file_name, 'w') as outfile:
        for line in infile:
            for (word_to_replace, replacement_word) in replacement_dictionary.items():
                while word_to_replace in line:
                    line = line.replace(word_to_replace, replacement_word, 1)
                    number_of_replacements += 1
            outfile.write(line)
    print("Number of replacements done: %d" % number_of_replacements)
    

def main():
    replacement_dictionary = read_replacement_file()
    output_file_name = input('Please enter the name of the output file: ')
    replace_words_and_write_to_file(output_file_name, replacement_dictionary)
        
### MAIN ###

if __name__ == '__main__':
    main()

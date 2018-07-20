#!/usr/bin/python3
# -*- coding: utf-8 -*-

PLEASE_ENTER_FILE = 'Please enter name of file to process: '

def get_non_empty_string_input(msg):
    done = False
    s = ""
    while not done:
        s = input(msg)
        s = s.strip()
        if len(s) > 0:
            done = True
    return s

def add_to_dict(frequency_to_word_dict, word, frequency):
    # Remove word from old frequency.
    if frequency > 1:
        frequency_to_word_dict[frequency - 1].remove(word)

    if frequency not in frequency_to_word_dict:
        # First time a word having this frequency being found?
        frequency_to_word_dict[frequency] = list()

        # Add word to new frequency.
    frequency_to_word_dict[frequency].append(word)
    
def open_and_process_file(filename):
    word_frequency_dict = dict()
    frequency_to_word_dict = dict()
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            for word in line.split():
                if word not in word_frequency_dict:
                    word_frequency_dict[word] = 1                    
                else:
                    word_frequency_dict[word] = word_frequency_dict[word] + 1

                add_to_dict(frequency_to_word_dict, word, word_frequency_dict[word])
                
    return (word_frequency_dict, frequency_to_word_dict)

#def display_results(sorted_list_of_words_in_frequency_order, word_frequency_dict):
#    for word in sorted_list_of_words_in_frequency_order:
#        print(word + ': ' + ('*' * word_frequency_dict[word]))

def display_results(frequency_to_word_dict):
    frequencies = list(frequency_to_word_dict.keys())
    frequencies.sort(reverse=True)
    for frequency in frequencies:
        words = frequency_to_word_dict[frequency]
        for word in words:
            print(word + ': ' + ('*' * frequency))

        
#def sort_keys_in_frequency_order(word_frequency_dict):
#    keys = list(word_frequency_dict.keys())
#    keys.sort() here sort in frequency order!
#    return keys

def main():
    filename = get_non_empty_string_input(PLEASE_ENTER_FILE)
    (word_frequency_dict, frequency_to_word_dict) = open_and_process_file(filename)
    display_results(frequency_to_word_dict)
    
### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

IN_FILE_NAME = 'inputFile.txt'
USE = 'use'
UTILIZE = 'utilize'

def main():
    number_of_replacements = 0
    output_file_name = input('Please enter the name of the output file: ')
    with open(IN_FILE_NAME, 'r') as infile, open(output_file_name, 'w') as outfile:
        for line in infile:
            while UTILIZE in line:
                line = line.replace(UTILIZE, USE, 1)
                number_of_replacements += 1
            outfile.write(line)
    print("Number of replacements done: %d" % number_of_replacements)
        
### MAIN ###

if __name__ == '__main__':
    main()

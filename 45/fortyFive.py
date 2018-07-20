#!/usr/bin/python3
# -*- coding: utf-8 -*-

IN_FILE_NAME = 'inputFile.txt'
USE = 'use'
UTILIZE = 'utilize'

def main():
    output_file_name = input('Please enter the name of the output file: ')
    with open(IN_FILE_NAME, 'r') as infile, open(output_file_name, 'w') as outfile:
        for line in infile:
            line = line.replace(UTILIZE, USE)
            outfile.write(line)
        
### MAIN ###

if __name__ == '__main__':
    main()

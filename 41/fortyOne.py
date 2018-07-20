#!/usr/bin/python3
# -*- coding: utf-8 -*-


IN_FILENAME = "persons.txt"
OUT_FILENAME = "personsSorted.txt"

FIRST_NAME = "firstName"
LAST_NAME = "lastName"

def write_data_to_file(persons):
    with open(OUT_FILENAME, 'w') as f:
        for person in persons:
            f.write(person[LAST_NAME])
            f.write(', ')
            f.write(person[FIRST_NAME])
            f.write('\n')

def read_data_from_file():
    persons = list()

    with open(IN_FILENAME, 'r') as f:
        for line in f:
            person_dict = dict()
            line = line.strip()
            fields = line.split(',')
            if len(fields) < 2:
                print("The following row in the indata file %s is malformed: " % IN_FILENAME)
                print(line)
                continue
            
            person_dict[LAST_NAME] = fields[0].strip()
            person_dict[FIRST_NAME] = fields[1].strip()

            persons.append(person_dict)
    return persons


def sort_persons(persons):
    sorted_persons = list()

    for person in persons:
        for (index, p2) in enumerate(sorted_persons):
            if person[LAST_NAME] < p2[LAST_NAME] or (person[LAST_NAME] == p2[LAST_NAME] and person[FIRST_NAME] < p2[FIRST_NAME]):
                sorted_persons.insert(index, person)
                break
        else:
            sorted_persons.append(person)
            
    return sorted_persons

def print_persons(persons):
    header_first_row = "Total of %d names" % len(persons)
    header_second_row = '-' * (len(header_first_row) + 1)
    print(header_first_row)
    print(header_second_row)

    for person in persons:
        print(person[LAST_NAME], end='')
        print(', ', end='')
        print(person[FIRST_NAME])
        
def main():
    persons = read_data_from_file()
    sorted_persons = sort_persons(persons)
    print_persons(sorted_persons)
    write_data_to_file(sorted_persons)
    
### MAIN ###

if __name__ == '__main__':
    main()

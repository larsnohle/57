persons = list()

#John Johnson Manager 2016-12-31
#Tou Xiong Software Engineer 2016-10-05
#Michaela Michaelson District Manager 2015-12-19
# Jake Jacobson Programmer
#Jacquelyn Jackson DBA
#Sally Weber Web Developer 2015-12-18

FIRST_NAME = "firstName"
LAST_NAME = "lastName"
POSITION = "position"
SEPARATION_DATE = "separationDate"
persons.append({FIRST_NAME : "John", LAST_NAME: "Johnson", POSITION: "Manager", SEPARATION_DATE: " 2016-12-31"})
persons.append({FIRST_NAME : "Tou", LAST_NAME: "Xiong", POSITION: "Software Engineer", SEPARATION_DATE: "2016-10-05"})
persons.append({FIRST_NAME : "Michaela", LAST_NAME: "Michaelson", POSITION: "District Manager", SEPARATION_DATE: "2015-12-19"})
persons.append({FIRST_NAME : "Jake", LAST_NAME: "Jacobson", POSITION: "Programmer"})
persons.append({FIRST_NAME : "Jacquelyn", LAST_NAME: "Jackson", POSITION: "DBA"})
persons.append({FIRST_NAME : "Sally", LAST_NAME: "Weber", POSITION: "Web Developer", SEPARATION_DATE: "2015-12-18"})

#!/usr/bin/python3
# -*- coding: utf-8 -*-

def sort_based_on_last_name():
    sorted_persons = list()
    
    sorted_persons.append(persons[0])
    index = 1
    while index < len(persons):
        j = 0
        person_to_insert = persons[index]
        insertion_position_found = False
        while insertion_position_found == False and j < len(sorted_persons):
            if person_to_insert[LAST_NAME] < sorted_persons[j][LAST_NAME]:
                insertion_position_found = True
                sorted_persons.insert(j, person_to_insert)

            j += 1

        if insertion_position_found == False:
            sorted_persons.append(person_to_insert)
        index += 1
    return sorted_persons

def print_header():
    print("Name                | Position          | Separation Date")
    print("--------------------|-------------------|----------------")

def print_person(person):
    pass

def longest_first_name():
    max_so_far = 0
    for person in persons:
        if len(person[FIRST_NAME]) > max_so_far:
            max_so_far = len(person[FIRST_NAME])

    return max_so_farx

def longest_last_name():
    max_so_far = 0
    for person in persons:
        if len(person[LAST_NAME]) > max_so_far:
            max_so_far = len(person[LAST_NAME])

    return max_so_farx


here

def main():
    sorted_persons = sort_based_on_last_name()
    for person in sorted_persons:
        print(person[LAST_NAME])
    
### MAIN ###

if __name__ == '__main__':
    main()

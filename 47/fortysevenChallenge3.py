#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.client
import json 

MAIN_URL = 'api.open-notify.org'
SUB_URL = '/astros.json'
NAME = 'name'
PEOPLE = 'people'
CRAFT = 'craft'

def find_len_of_longest_property_value(person_and_craft_list, name_of_property):
    max_so_far = 0
    for person_and_craft in person_and_craft_list:
        length_of_name = len(person_and_craft[name_of_property])
        if length_of_name > max_so_far:
            max_so_far = length_of_name
    return max_so_far

def read_data_from_url():
    conn = http.client.HTTPConnection(MAIN_URL)
    conn.request("GET", SUB_URL)
    response = conn.getresponse()
    data = response.read().decode() # To translate from binary string to regular string.
    return data

def display_result(craft_to_persons_dict, number_of_persons, len_of_longest_name, len_of_longest_craft):
    print("There are %d people in space right now:" % number_of_persons)
    print()
    print('Name', end='')
    print(' ' * (len_of_longest_name - len('name') + 1), end = '')
    print('| ', end = '')
    print('Craft')
    
    print('-' * (len_of_longest_name + 1), end = '')
    print('|', end = '')
    l = len_of_longest_craft
    if len(CRAFT) > len_of_longest_craft:
        l = len(CRAFT)
    print('-' * (l + 1))

    for craft in craft_to_persons_dict.keys():
        for (index, person) in enumerate(craft_to_persons_dict[craft]):
            print(person, end='')
            print(" " * (len_of_longest_name - len(person) + 1), end='')
            print('|', end = '')
            if index == 0:
                print(craft, end='')
            print()

def collect_by_craft(person_and_craft_list):
    craft_to_persons_dict = dict()
    for person_and_craft in person_and_craft_list:
        person = person_and_craft[NAME]
        craft = person_and_craft[CRAFT]
        if craft not in craft_to_persons_dict:
            persons_for_craft = list()
            craft_to_persons_dict[craft] = persons_for_craft
        persons_for_craft = craft_to_persons_dict[craft]
        persons_for_craft.append(person)
    return craft_to_persons_dict

def extract_last_name(full_name):
    name_parts = full_name.split(' ')
    number_of_name_parts = len(name_parts)
    if number_of_name_parts % 2 == 0:
        first_index = int(number_of_name_parts / 2)
    else:
        first_index = int(number_of_name_parts / 2 + 1)
    return ' '.join(name_parts[first_index:])

def sort_by_last_name(craft_to_persons_dict):
    craft_to_sorted_persons_dict = dict(craft_to_persons_dict)
    for (craft, persons) in craft_to_persons_dict.items():
        sorted_persons = sorted(persons, key=extract_last_name)
        craft_to_sorted_persons_dict[craft] = sorted_persons        
    return craft_to_sorted_persons_dict

def main():
    data = read_data_from_url()
    data_as_object = json.loads(data)
    person_and_craft_list = data_as_object[PEOPLE]
    len_of_longest_name = find_len_of_longest_property_value(person_and_craft_list, NAME)
    len_of_longest_craft = find_len_of_longest_property_value(person_and_craft_list, CRAFT)
    craft_to_persons_dict = collect_by_craft(person_and_craft_list)
    craft_to_persons_dict = sort_by_last_name(craft_to_persons_dict)
    display_result(craft_to_persons_dict, len(person_and_craft_list), len_of_longest_name, len_of_longest_craft)
    
### MAIN ###

if __name__ == '__main__':
    main()

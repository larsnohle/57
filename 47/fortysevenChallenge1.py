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


def display_result(person_and_craft_list, len_of_longest_name, len_of_longest_craft):
    print("There are %d people in space right now:" % len(person_and_craft_list))
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

    for person_and_craft in person_and_craft_list:
        person = person_and_craft[NAME]
        craft = person_and_craft[CRAFT]
        print(person, end='')
        print(" " * (len_of_longest_name - len(person) + 1), end='')
        print('|', end = '')
        print(craft)
    
    

def main():
    data = read_data_from_url()
    data_as_object = json.loads(data)
    person_and_craft_list = data_as_object[PEOPLE]
    len_of_longest_name = find_len_of_longest_property_value(person_and_craft_list, NAME)
    len_of_longest_craft = find_len_of_longest_property_value(person_and_craft_list, CRAFT)
    display_result(person_and_craft_list, len_of_longest_name, len_of_longest_craft)
    
### MAIN ###

if __name__ == '__main__':
    main()

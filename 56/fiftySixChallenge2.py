#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os.path
import json

# CONSTANTS
ENTER_ITEM_CHOICE = '1'
DISPLAY_REPORT_IN_CSV_CHOICE = '2'
DISPLAY_REPORT_IN_HTML_CHOICE = '3'
DISPLAY_REPORT_IN_HTML_CHOICE = '3'
DISPLAY_REPORT_IN_TEXT_CHOICE = '4'
SEARCH_CHOICE = '5'
QUIT_CHOICE = 'q'
ALLOWED_RESPONSES= [ENTER_ITEM_CHOICE, DISPLAY_REPORT_IN_CSV_CHOICE, DISPLAY_REPORT_IN_HTML_CHOICE, DISPLAY_REPORT_IN_TEXT_CHOICE, SEARCH_CHOICE, QUIT_CHOICE]

ITEM_NAME='itemName'
SERIAL_NUMBER='serialNumber'
VALUE='value'
ITEMS = 'items'
FILENAME = 'items.json'

NAME_COLUMN='Name'
SERIAL_NUMBER_COLUMN='SERIAL NUMBER'
VALUE_COLUMN='VALUE'

def initialize_items_dict():
    if not os.path.exists(FILENAME):
        print("Did not find file %s" % FILENAME)
        items_dict = {ITEMS: list()}
    else:    
        with open(FILENAME, 'r') as items_file:
            items_dict = json.load(items_file)
    return items_dict

def display_menu():
    print()
    print("*************************")
    print("*         MENU          *") 
    print("*************************")
    print("1) Enter item.")
    print("2) Print report in CSV format.")
    print("3) Print report in HTML format.")
    print("4) Print report in text format.")
    print("5) Search.")
    print("q) Quit")

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

# Get float input
def get_float_input(msg):
    done = False
    while not done:
        try:
            i = float(input(msg))
            done = True
        except ValueError:
            print("That was not a valid float. Please try again!")

    return i

def write_items_dict_to_file(items_dict):
    with open(FILENAME, 'w') as f:
        json.dump(items_dict, f)

def enter_item(items_dict):
    item_name = get_non_empty_string_input('Please enter item name: ')
    serial_number = get_non_empty_string_input('Please enter serial number: ')
    value = get_float_input('Please enter (numeric) value: ')
    item_dict = {ITEM_NAME: item_name,
                 SERIAL_NUMBER: serial_number,
                 VALUE: value}
    
    items_dict[ITEMS].append(item_dict)
    write_items_dict_to_file(items_dict)
    return items_dict

def max_value(x, y):
    if x > y:
        return x
    return y

def find_length_of_longest_item_name(items_dict):
    return max_value(find_length_of_longest_value_of_an_attribute(items_dict, ITEM_NAME), len(NAME_COLUMN))

def find_length_of_longest_serial_number(items_dict):
    return max_value(find_length_of_longest_value_of_an_attribute(items_dict, SERIAL_NUMBER), len(SERIAL_NUMBER_COLUMN))

def find_length_of_longest_value(items_dict):
    return max_value(find_length_of_longest_value_of_an_attribute(items_dict, VALUE), len(VALUE_COLUMN))

def find_length_of_longest_value_of_an_attribute(items_dict, attribute):
    longest_length_so_far = 0
    for item in items_dict[ITEMS]:
        if len(str(item[attribute])) > longest_length_so_far:
            longest_length_so_far = len(str(item[attribute]))
    return longest_length_so_far

def print_report_in_csv_format(items_dict):    
    for item in items_dict[ITEMS]:
        print(item[ITEM_NAME], end='')
        print(',', end='')
        print(item[SERIAL_NUMBER], end='')
        print(',', end='')
        print(item[VALUE])
    print()

def print_report_in_html_format(items_dict):
    print("<html>")
    print("<body>")
    print("<table>")
    print("<tr><th>%s</th><th>%s</th><th>%s</th></tr>" % (NAME_COLUMN, SERIAL_NUMBER_COLUMN, VALUE_COLUMN))
    for item in items_dict[ITEMS]:
        print("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (item[ITEM_NAME], item[SERIAL_NUMBER], item[VALUE]))
    print("</table>")
    print("</body>")
    print("</html>")

def print_report_in_text_format(items_dict):
    name_column_len = find_length_of_longest_item_name(items_dict) + 1
    serial_number_column_len = find_length_of_longest_serial_number(items_dict) + 1
    value_column_len = find_length_of_longest_value(items_dict) + 1

    print('=' * (name_column_len + serial_number_column_len + value_column_len))
    print('NAME', end='')
    print(' ' * (name_column_len - len('NAME')), end='')
    print('SERIAL NUMBER', end='')
    print(' ' * (serial_number_column_len - len('SERIAL NUMBER')), end='')
    print('VALUE')    
#    print(' ' * (value_column_len - len('VALUE')))
    
    for item in items_dict[ITEMS]:
        print(item[ITEM_NAME], end='')
        print(' ' * (name_column_len - len(item[ITEM_NAME])), end='')
        print(item[SERIAL_NUMBER], end='')
        print(' ' * (serial_number_column_len - len(item[SERIAL_NUMBER])), end='')
        print(item[VALUE])
    print('=' * (name_column_len + serial_number_column_len + value_column_len))

def search(items_dict):
    text_to_search_for = get_non_empty_string_input('Please enter text to search for: ')
    search_result_dict = {ITEMS: list()}
    for item in items_dict[ITEMS]:
        if text_to_search_for in item[ITEM_NAME] or text_to_search_for in item[SERIAL_NUMBER] or text_to_search_for in str(item[VALUE]):
            item_dict = {ITEM_NAME: item[ITEM_NAME],
                         SERIAL_NUMBER: item[SERIAL_NUMBER],
                         VALUE: item[VALUE]}
            search_result_dict[ITEMS].append(item_dict)
    print_report_in_text_format(search_result_dict)
    
def main():
    items_dict = initialize_items_dict()
    done = False
    while not done:
        display_menu()
        choice = get_string_input('Choice: ', ALLOWED_RESPONSES)
        if choice == QUIT_CHOICE:
            done = True
        elif choice == ENTER_ITEM_CHOICE:
            items_dict = enter_item(items_dict)
        elif choice == DISPLAY_REPORT_IN_CSV_CHOICE:
            print_report_in_csv_format(items_dict)
        elif choice == DISPLAY_REPORT_IN_HTML_CHOICE:
            print_report_in_html_format(items_dict)
        elif choice == DISPLAY_REPORT_IN_TEXT_CHOICE:
            print_report_in_text_format(items_dict)
        elif choice == SEARCH_CHOICE:
            search(items_dict)


### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

INPUT_FILE_NAME = "products.json"
OUTPUT_FILE_NAME = "products.json"

ENTER_PRODUCT_NAME = 'What is the product name? '
ERROR_MESSAGE = 'Sorry, that product was not found in our inventory.'
PRODUCTS = 'products'
NAME = 'name'
PRICE = 'price'
QUANTITY = 'quantity'
NAME_CAPITALIZED = 'Name: '
PRICE_CAPITALIZED = 'Price: '
QUANTITY_CAPITALIZED = 'Quantity on hand: '

def read_json_file():
    json_payload = None
    with open(INPUT_FILE_NAME, 'r') as json_file:
        json_payload = json.load(json_file)
    return json_payload

def write_to_json_file(product_dict):
    with open(OUTPUT_FILE_NAME, 'w') as f:
        json.dump(product_dict, f)

def create_product_dict(products_as_json):
    product_dict = dict()
    product_array = products_as_json[PRODUCTS]
    for product in product_array:
        product_dict[product[NAME].upper()] = product

    return product_dict

def format_price(price):
    p = '{:.2f}'.format(float(price))
    return '$' + p

def print_product(product):
    print(NAME_CAPITALIZED, end='')
    print(product[NAME])
    print(PRICE_CAPITALIZED, end='')
    print(format_price(product[PRICE]))
    print(QUANTITY_CAPITALIZED, end='')
    print(product[QUANTITY])

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def get_integer_input(msg):
    done = False
    while not done:
        try:
            i = int(input(msg))
            done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")

    return i
    
def should_add_product(product_name):
    add_product = get_string_input('Should the product named %s be added to the json file? [y/n] : ' % product_name, ['y', 'n'])
    if add_product.upper() == 'Y':
        return True

    return False

def read_data_about_product_and_add_it(product_name, product_dict):
    price = get_integer_input('Please enter the price: ')
    quantity = get_integer_input('Please enter the quantity: ')
    product_to_add = dict()
    product_to_add[NAME] = product_name
    product_to_add[PRICE] = price
    product_to_add[QUANTITY] = quantity
    product_dict[product_name.upper()] = product_to_add

    dict_to_write = dict()
    products_list = list(product_dict.values())
    dict_to_write[PRODUCTS] = products_list

    write_to_json_file(dict_to_write) 

def loop_until_product_found(product_dict):
    product_found = False
    while not product_found:
        product_name = input(ENTER_PRODUCT_NAME)
        if product_name.upper() in product_dict:
            product_found = True
            print_product(product_dict[product_name.upper()])
        elif should_add_product(product_name):
            read_data_about_product_and_add_it(product_name, product_dict)

def main():
    products_as_json = read_json_file()
    product_dict = create_product_dict(products_as_json)
    loop_until_product_found(product_dict)
    
### MAIN ###

if __name__ == '__main__':
    main()

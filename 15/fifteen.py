#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    username_lookup = {}
    username_lookup["lars"] = "larsPassword"

    username = input("Username: ")
    password = input("Password: ")

    if username in username_lookup and username_lookup[username] == password:
        print("Welcome!")
    else:
        print("I don’t know you.")

### MAIN ###

if __name__ == '__main__':
    main()

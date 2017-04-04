#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Same as fifteenChallenge1 as the un/pw:s are already stored in a dict.

import getpass

def main():
    username_lookup = {}
    username_lookup["lars"] = "larsPassword"

    username = input("Username: ")
    password = getpass.getpass("Password: ") 

    if username in username_lookup and username_lookup[username] == password:
        print("Welcome!")
    else:
        print("I don’t know you.")

### MAIN ###

if __name__ == '__main__':
    main()

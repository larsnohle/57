#!/usr/bin/python
# -*- coding: utf-8 -*-

# Run with Python2. I could not get pip3 to install bcrypt...

import getpass
import bcrypt

def main():
    username_lookup = {}
    username_lookup["lars"] = bcrypt.hashpw("larsPassword", bcrypt.gensalt())

    username = raw_input("Username: ")
    password = getpass.getpass("Password: ") 

#    print "In dict: %s " % username_lookup[username]
#    print "Hashed: %s" % bcrypt.hashpw(password, username_lookup[username])

    # This is the way to compare hashes.
    if username in username_lookup and bcrypt.hashpw(password, username_lookup[username]) == username_lookup[username]:
        print("Welcome!")
    else:
        print("I don’t know you.")

### MAIN ###

if __name__ == '__main__':
    main()

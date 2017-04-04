#!/usr/bin/python3
# -*- coding: utf-8 -*-

def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    if len(first_string) == 0:
        return False

    first_set = set()
    for s in first_string:
        first_set.add(s)

    second_set = set()
    for s in second_string:
        second_set.add(s)

    if len(first_set.difference(second_set)) == 0:
        return True

    return False


def main():
    print("Enter two strings and I'll tell you if they are anagrams")
    first_string = input("Enter the first string: ")
    second_string = input("Enter the second string: ")

    if is_anagram(first_string, second_string):
        print("\"%s\"  and \"%s\" are anagrams" % (first_string, second_string))
    else:
        print("\"%s\"  and \"%s\" are NOT anagrams" % (first_string, second_string))


### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

INDEX_FILE = 'index.html'
META_CONTENT = 'META_CONTENT'
TITLE_CONTENT = 'TITLE_CONTENT'

INDEX_TEMPLATE = """<html>
<head>
<meta>META_CONTENT</meta>
 <title>TITLE_CONTENT</title>
</head>
</html>
"""


def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def get_boolean_input(msg):
    done = False
    s = ""
    allowed_responses = ['y','Y','n','N']
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
            
    return s == 'Y' or s == 'y'


def get_input():
    site_name = input("Site name: ")
    author = input("Author: ")        
    create_java_script_dir = get_boolean_input('Do you want a folder for JavaScript (y/n)?: ')
    create_css_dir = get_boolean_input('Do you want a folder for CSS(y/n)?:')
    return (site_name, author, create_java_script_dir, create_css_dir)

def create_content(site_name, author, create_java_script_dir, create_css_dir):
    os.mkdir(site_name)
    if create_java_script_dir:
        os.mkdir(site_name + '/' + 'js')

    if create_css_dir:
        os.mkdir(site_name + '/' + 'css')

    content = INDEX_TEMPLATE.replace(META_CONTENT, author)
    content = content.replace(TITLE_CONTENT, site_name)
    with open(site_name + '/' + INDEX_FILE, 'w') as f:
        f.write(content)
    

def main():
    (site_name, author, create_java_script_dir, create_css_dir) = get_input()
    create_content(site_name, author, create_java_script_dir, create_css_dir)

### MAIN ###

if __name__ == '__main__':
    main()

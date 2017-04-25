#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

def get_string_input(msg, allowed_responses):
    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True
    return s

def create_main_dir(site_name):
    main_dir = "./" + site_name
    os.mkdir(main_dir)
    print("Created %s" % main_dir)

def create_supplementary_dirs(site_name, should_java_script_dir_be_generated, should_css_dir_be_generated):
    if should_java_script_dir_be_generated == 'y' or should_java_script_dir_be_generated == 'Y':
        java_script_dir = "./" + site_name + "/" + "js" + "/"
        os.mkdir(java_script_dir)
        print("Created %s" % java_script_dir)
    if should_css_dir_be_generated == 'y' or should_css_dir_be_generated == 'Y':
        css_dir = "./" + site_name + "/" + "css" + "/"
        os.mkdir(css_dir)
        print("Created %s" % css_dir)

def create_index_file(site_name, author):
    f = open(site_name + "/index.html", 'w')
    index_file_content = """
    <html>
    <head>
    <title>%s</title>
    <meta name="author" content="%s">
    </head>
    </html>
    """ % (site_name, author)
    f.write(index_file_content)

def main():
    site_name = input("Site name: ")
    author = input("Author: ")
    should_java_script_dir_be_generated = get_string_input("Do you want a folder for JavaScript? ", ['y', 'Y', 'n', 'N'])
    should_css_dir_be_generated = get_string_input("Do you want a folder for CSS? ", ['y', 'Y', 'n', 'N'])

    create_main_dir(site_name)
    create_supplementary_dirs(site_name, should_java_script_dir_be_generated, should_css_dir_be_generated)
    create_index_file(site_name, author)
    
### MAIN ###

if __name__ == '__main__':
    main()


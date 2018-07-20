#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

line = '<link rel="enclosure" type="image/jpeg" href="http://farm1.staticflickr.com/922/43158356892_5618f39c99_b.jpg" />'
image_link_reg_exp = re.compile('link .* href=\\"(.*\\.jpg)\\".*')

def main():
    if image_link_reg_exp.match(employee_id):
        print("Matches!")
    else:
        print("No match!")

### MAIN ###

if __name__ == '__main__':
    main()

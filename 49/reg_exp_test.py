#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

line = '<link rel="enclosure" type="image/jpeg" href="http://farm1.staticflickr.com/922/43158356892_5618f39c99_b.jpg" />'
#image_link_reg_exp = re.compile('.*link .* href=\\"http(s)*://([^/]+)(.*\\.jpg)\\".*')
image_link_reg_exp = re.compile('.*img src=&quot;http(s)*://([^/]+)(.*\\.jpg)&quot;.*')
line2='&lt;p&gt;&lt;a href=&quot;http://www.flickr.com/photos/141255470@N06/42489418484/&quot; title=&quot;Sunset Jetties And Sky&quot;&gt;&lt;img src=&quot;http://farm2.staticflickr.com/1829/42489418484_b3ffaf5702_m.jpg&quot; width=&quot;240&quot; height=&quot;180&quot; alt=&quot;Sunset Jetties And Sky&quot; /&gt;&lt;/a&gt;&lt;/p&gt;'

line3="""&lt;p&gt;&lt;a href=&quot;http://www.flickr.com/photos/75426780@N02/28358935117/&quot; title=&quot;&quot;&gt;&lt;img src=&quot;http://farm1.staticflickr.com/918/28358935117_99a77e8027_m.jpg&quot; width=&quot;240&quot; height=&quot;160&quot; alt=&quot;&quot; /&gt;&lt;/a&gt;&lt;/p&gt;"""
def main():
    match = image_link_reg_exp.match(line3)
    if match:
        print("Matches!")
        domain = match.group(2)
        path = match.group(3)
        print(domain)
        print(path)
    else:
        print("No match!")

### MAIN ###

if __name__ == '__main__':
    main()

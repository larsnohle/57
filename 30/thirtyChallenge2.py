#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    s = "\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\n"
    for row in range(0, 13):
        s += str(row)
        s += "\t"
        for col in range(0, 13):            
            s += str(row * col)
            s += "\t"
        s += "\n"
    print(s)

### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math

def min(values):
    if len(values) == 0:
        return None

    min_so_far = values[0]
    for value in values:
        if value < min_so_far:
            min_so_far = value

    return min_so_far

def max(values):
    if len(values) == 0:
        return None

    max_so_far = values[0]
    for value in values:
        if value > max_so_far:
            max_so_far = value

    return max_so_far

def mean(values):
    if len(values) == 0:
        return None

    sum = 0
    for value in values:
        sum += value
    return sum / len(values)

def standard_deviation(values, mean_value):
    if len(values) == 0:
        return None

    s = 0
    for value in values:
        s += ((value - mean_value) ** 2)
        
    return math.sqrt(s / len(values))



def main():
    done = False
    values = list()
    while not done:
        try:
            value = input("Enter a value: ")    
            if value.strip() == 'done':
                done = True
            else:
                values.append(int(value))
        except EOFError:
            done = True

    mean_value =  mean(values)
    print("The mean is %f" % mean_value)
    print("The max is %d" % max(values))
    print("The mim is %d" % min(values))
    print("The standard deviation is %f" % standard_deviation(values, mean_value))

    
        
### MAIN ###

if __name__ == '__main__':
    main()




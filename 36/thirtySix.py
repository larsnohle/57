#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math

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

    sum = 0
    min = None
    max = None
    for value in values:
        sum += value
        if max == None or value > max:
            max = value

        if min == None or value < min:
            min = value

    mean = float(sum) / len(values)

    # Calculate variance.
    sum_of_values_minus_mean_squrared = 0
    for value in values:
        sum_of_values_minus_mean_squrared += (value - mean) ** 2

    variance = float(sum_of_values_minus_mean_squrared) / len(values)
    standard_deviation = math.sqrt(variance)
        
    print("The sum is %d" % sum)
    print("The mean is %f" % mean)
    print("The max is %d" % max)
    print("The mim is %d" % min)
    print("The standard deviation is %f" % standard_deviation)

    
        
### MAIN ###

if __name__ == '__main__':
    main()




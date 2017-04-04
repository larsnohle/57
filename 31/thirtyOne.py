#!/usr/bin/python3
# -*- coding: utf-8 -*-

def get_positive_number_input(msg, to_float = False):
    done = False
    while not done:
        try:
            i = -1.0
            if to_float == True:
                i = float(input(msg))
            else:
                i = int(input(msg))
            if i < 0:
                print("Please enter a number > 0")
            else:
                done = True
        except ValueError:
            print("That was not a valid integer. Please try again!")

    return i


def main():
    age = get_positive_number_input("Age: ")
    resting_heart_rate = get_positive_number_input("Resting heart rate: ")
    
    print("Resting Pulse: 65 Age: 22")
    print("")
    print("Intensity    | Rate")
    print("-------------|--------")
    
    for intensity in range(55, 100, 5):
        target_heart_rate = (((220 - age) - resting_heart_rate) * intensity / 100) + resting_heart_rate
        print("%d %%         | %d bpm" % (intensity, target_heart_rate))

### MAIN ###

if __name__ == '__main__':
    main()

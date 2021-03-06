#!/usr/bin/python3
# -*- coding: utf-8 -*-

car_silent_question = "Is the car silent when you turn the key? "

battery_terminals_corroded_question = "Are the battery terminals corroded? "
clicking_noise_question = "Does the car make a clicking noise? "

clean_battery_terminals = "Clean terminals and try starting again."
battery_cables_corroded = "The battery cables may be damaged."
replace_battery_cables = "Replace cables and try again."
replace_battery = "Replace the battery."
car_cranks_question = "Does the car crank up but fail to start? "

check_spark_plug_connections = "Check spark plug connections."
engine_starts_but_dies_question = "Does the engine start and then die? "

check_choke = "Check to ensure the choke is opening and closing."
get_service = "Get it in for service."

car_has_fuel_injection_question = "Does your car have fuel injection? "


def get_boolean_input(msg):
    allowed_responses = ["y", "Y", "n", "N"]

    done = False
    s = ""
    while not done:
        s = input(msg)
        if s in allowed_responses:
            done = True

    return s == 'y' or s == 'Y'

def handle_car_start_but_dies():
    car_has_fuel_injection = get_boolean_input(car_has_fuel_injection_question)
    if car_has_fuel_injection == True:
        print(get_service)
    else:
        print(check_choke)

def handle_car_does_not_crank():
   engine_starts_but_dies  = get_boolean_input(engine_starts_but_dies_question)
   if engine_starts_but_dies == True:
       handle_car_start_but_dies()
   else:
       print(get_service)
        

def handle_battery_terminals_corroded():
    print(clean_battery_terminals + "\n")

def handle_battery_terminals_not_corroded():
    print(battery_cables_corroded + "\n" + replace_battery_cables + "\n")

def handle_car_silent():
    corroded_terminals = get_boolean_input(battery_terminals_corroded_question)
    if corroded_terminals == True:
        handle_battery_terminals_corroded()
    else:
        handle_battery_terminals_not_corroded()

def handle_clicking_noise():
    print(replace_battery)

def handle_not_clicking_noise():
    car_cranks = get_boolean_input(car_cranks_question)
    if car_cranks == True:
        print(check_spark_plug_connections)
    else:
        handle_car_does_not_crank()
            
def handle_car_not_silent():
    clicking_noise = get_boolean_input(clicking_noise_question)
    
    if clicking_noise == True:
        handle_clicking_noise()
    else:
        handle_not_clicking_noise()

def main():
    car_silent = get_boolean_input(car_silent_question)

    if car_silent == True:
        handle_car_silent()
    else:
        handle_car_not_silent()

### MAIN ###

if __name__ == '__main__':
    main()



#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Where are you? London
#{
#"coord":{"lon":-0.13,"lat":51.51},
#"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
#"base":"stations",
#"main":
#{"temp":299.72,"pressure":1013,"humidity":41,"temp_min":296.15,"temp_max":303.15},"visibility":10000,
#  "wind":{"speed":6.2,"deg":90},
#  "clouds":{"all":68},"dt":1530467400,
#  "sys":{"type":1,"id":5091,"message":0.0032,"country":"GB","sunrise":1530416883,"sunset":1530476439},"id":2643743,"name":"London","cod":200}


import http.client
import json
import time

MAIN_URL = 'api.openweathermap.org'
SUB_URL = '/data/2.5/weather?'
API_KEY='8028ac32013fb0a39f9043a36198a213'
START_OF_QUERY_STRING='APPID=' + API_KEY + '&q='
KELVIN_TO_CELSIUS_DIFF=273.15

def kelvin_to_celsius(kelvin):
    return kelvin - KELVIN_TO_CELSIUS_DIFF

def epoch_to_printable_time(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))

def degrees_to_wind_direction_in_words(degrees):
    degrees = float(degrees % 360)
    if degrees > 337.5 or degrees <= 22.5:
        wind_direction = 'East'
    elif degrees > 22.5 and degrees <= 67.5:
        wind_direction = 'NorthEast'
    elif degrees > 67.5 and degrees <= 112.5:
        wind_direction = 'North'
    elif degrees > 112.5 and degrees <= 157.5:
        wind_direction = 'NorthWest'
    elif degrees > 157.5 and degrees <= 202.5:
        wind_direction = 'West'
    elif degrees > 202.5 and degrees <= 247.5:
        wind_direction = 'SouthWest'
    elif degrees > 247.5 and degrees <= 292.5:
        wind_direction = 'South'
    elif degrees > 292.5 and degrees <= 337.5:
        wind_direction = 'SouthEast'
        
    return wind_direction

def get_non_empty_string_input(msg):
    done = False
    s = ""
    while not done:
        s = input(msg)
        s = s.strip()
        if len(s) > 0:
            done = True
    return s

def get_weather_for_location(location):
    conn = http.client.HTTPConnection(MAIN_URL)
    query_string = START_OF_QUERY_STRING + location
    conn.request("GET", SUB_URL + query_string)
    response = conn.getresponse()    
    data = response.read().decode() # To translate from binary string to regular string.
#    print(data)
    data_as_object = json.loads(data)
    return data_as_object

def extract_temperature(weather):
    return float(weather['main']['temp'])

def extract_sunrise(weather):
    return float(weather['sys']['sunrise'])

def extract_sunset(weather):
    return float(weather['sys']['sunset'])

def extract_humidity(weather):
    return float(weather['main']['humidity'])

def extract_description(weather):
    return weather['weather'][0]['description']
def extract_wind_direction(weather):
    return int(weather['wind']['deg'])
    
def print_weather(location, weather):
    temperature = extract_temperature(weather)
    temperature_in_celsius = kelvin_to_celsius(temperature)
    print(location + ' weather:')
    print("%d degrees celsius" % int(temperature_in_celsius))
    print("Wind direction: " + degrees_to_wind_direction_in_words(extract_wind_direction(weather)))
    print("Sunrise: " + epoch_to_printable_time(extract_sunrise(weather)))
    print("Sunset: " + epoch_to_printable_time(extract_sunset(weather)))
    print("Humidity: %d" % extract_humidity(weather))
    print("Description: " + extract_description(weather))
    print("Categorization: " + categorize_weather(weather))
#    print(weather)

def categorize_weather(weather):
    description = extract_description(weather)
    categorization = ''
    if 'rain' in description:
        categorization = 'Rainy, '
    elif 'cloud' in description:
        categorization = 'Cloudy, '
    elif 'clear sky' in desctiption:
        categorization = 'Nice, '
        
    temperature = extract_temperature(weather)
    temperature_in_celsius = kelvin_to_celsius(temperature)
    if temperature_in_celsius < 0:
        categorization += 'cold'
    elif temperature_in_celsius < 20:
        categorization += 'normal temp'
    else:
        categorization += 'warm'

    return categorization
        
def main():
    location = get_non_empty_string_input('Where are you? ')
    weather = get_weather_for_location(location)
    print_weather(location, weather)

### MAIN ###

if __name__ == '__main__':
    main()

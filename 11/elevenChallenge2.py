import math
import urllib.request
import json

### FUNCTIONS ###

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

def get_rate_from_dict(exchange_rate_dict):
    done = False
    rate = None
    while not done:
        country = input("What country's currency are you exchanging? ")
        if country in exchange_rate_dict:
            rate = exchange_rate_dict[country]
            done = True
        else:
            print("Sorry, don't have any exchange rate for %s " % country)
        
    return rate

### MAIN ###

# Open connectoring to the webserver at open exchange.
open_exchange_app_id = "5e432fbaf6544dc7b084e8190dfd79fd"
url_to_exchange_service = "https://openexchangerates.org/api/latest.json?app_id=%s" % open_exchange_app_id
req = urllib.request.Request(url_to_exchange_service)

# Extract content. As the result is a binary string, we have to decode it to get a regular string.
with urllib.request.urlopen(req) as response:
    the_page = response.read().decode()

print(the_page)

payload_as_object = json.loads(the_page)

conversion_dict = payload_as_object["rates"]

# Get input.
amount = get_positive_number_input("What amount of money are you exchanging? ")

exchange_rate = get_rate_from_dict(conversion_dict)

# # Perform calculations.
number_of_dollars = amount / exchange_rate

# Print output.
print("%d at an exchange rate of %.2f is %.2f U.S. dollars." % (amount, exchange_rate, number_of_dollars))

import datetime;
import random
import urllib.parse

import hashlib
import hmac
import base64

lower_case_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
upper_case_letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sequences_to_pick_data_from = [lower_case_letters, upper_case_letters, digits]
NONCE_LENGTH = 32
CONSUMER_SECRET= 'H1Rpj7fvty14DfRikMWnRHQpjU6Tz0DieHAGLK3snR8Dy78uy9'
ACCESS_TOKEN_SECRET= '0ZvyCgirK5iTYDTpZQpcItY7ENmM8NsEE0d6JLgeDhCtA'
SIGNING_KEY= CONSUMER_SECRET + '&' + ACCESS_TOKEN_SECRET

# 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'
HTTP_METHOD='GET'
TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'
TWITTER_URL_PERCENT_ENCODED = 'https%3A%2F%2Fapi.twitter.com%2F1.1%2Fsearch%2Ftweets.json'

Q_KEY = 'q'
RESULT_TYPE_KEY = 'result_type'
OAUTH_CONSUMER_KEY_KEY = 'oauth_consumer_key' 	
OAUTH_NONCE_KEY = 'oauth_nonce'
OAUTH_SIGNATURE_METHOD_KEY = 'oauth_signature_method'
OAUTH_TIMESTAMP_KEY = 'oauth_timestamp' 	
OAUTH_TOKEN_KEY = 'oauth_token' 	
OAUTH_VERSION_KEY ='oauth_version'

Q_VALUE = 'nasa'
RESULT_TYPE_VALUE = 'popular'
OAUTH_CONSUMER_KEY_VALUE = 'maDF5Ns7UrP3atWzCt7wJwZ5c'
OAUTH_NONCE_VALUE = ''
OAUTH_SIGNATURE_METHOD_VALUE = 'HMAC-SHA1'
OAUTH_TIMESTAMP_VALUE = ''
OAUTH_TOKEN_VALUE = '1589408701-QQpGPWp04Cc6KtRpNPl3lLJoQjdT3BaWtdVBrTn' 	
OAUTH_VERSION_VALUE ='1.0'

PARAMETER_KEYS = list()
PARAMETER_KEYS.append(Q_KEY)
PARAMETER_KEYS.append(RESULT_TYPE_KEY)
PARAMETER_KEYS.append(OAUTH_CONSUMER_KEY_KEY)
PARAMETER_KEYS.append(OAUTH_NONCE_KEY)
PARAMETER_KEYS.append(OAUTH_SIGNATURE_METHOD_KEY)
PARAMETER_KEYS.append(OAUTH_TIMESTAMP_KEY)
PARAMETER_KEYS.append(OAUTH_TOKEN_KEY)
PARAMETER_KEYS.append(OAUTH_VERSION_KEY)

PARAMETER_DICT = dict()
PARAMETER_DICT[Q_KEY] = Q_VALUE
PARAMETER_DICT[RESULT_TYPE_KEY] = RESULT_TYPE_VALUE
PARAMETER_DICT[OAUTH_CONSUMER_KEY_KEY] = OAUTH_CONSUMER_KEY_VALUE
PARAMETER_DICT[OAUTH_NONCE_KEY] = OAUTH_NONCE_VALUE
PARAMETER_DICT[OAUTH_SIGNATURE_METHOD_KEY] = OAUTH_SIGNATURE_METHOD_VALUE
PARAMETER_DICT[OAUTH_TIMESTAMP_KEY] = OAUTH_TIMESTAMP_VALUE
PARAMETER_DICT[OAUTH_TOKEN_KEY] = OAUTH_TOKEN_VALUE
PARAMETER_DICT[OAUTH_VERSION_KEY] = OAUTH_VERSION_VALUE

AUTHORIZATION_HEADER_TEMPLATE = 'authorization: OAuth oauth_consumer_key="maDF5Ns7UrP3atWzCt7wJwZ5c",  oauth_nonce="%s", oauth_signature="%s",  oauth_signature_method="HMAC-SHA1", oauth_timestamp="%s",  oauth_token="1589408701-QQpGPWp04Cc6KtRpNPl3lLJoQjdT3BaWtdVBrTn", oauth_version="1.0"'

CURL_REQUEST_TEMPLATE = "curl --request GET  --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'  --header '%s'"

# curl --request GET  --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'  --header 'authorization: OAuth oauth_consumer_key="maDF5Ns7UrP3atWzCt7wJwZ5c",  oauth_nonce="oQdC5xZ10DLhl2jMERIMej1py73fcLOl", oauth_signature="generated-signature",  oauth_signature_method="HMAC-SHA1", oauth_timestamp="1531215246",  oauth_token="1589408701-QQpGPWp04Cc6KtRpNPl3lLJoQjdT3BaWtdVBrTn", oauth_version="1.0"'

def generate_base64_encoded_hmac_string(message, key):
    key_as_bytes = bytes(key, 'UTF-8')
    message_as_bytes = bytes(message, 'UTF-8')
    
    digester = hmac.new(key_as_bytes, message_as_bytes, hashlib.sha1)
    signature_as_bytes = digester.digest()    
    signature_base64_encoded = base64.urlsafe_b64encode(signature_as_bytes)    
    return str(signature_base64_encoded, 'UTF-8')


def generate_random_string(length):
    l = list()
    for i in range(length):
        sequence = sequences_to_pick_data_from[random.randint(0, len(sequences_to_pick_data_from) - 1)]
        c = sequence[random.randint(0, len(sequence) - 1)]
        l.append(c)
    return ''.join(l)

def generate_timestamp():
    return int(datetime.datetime.now().timestamp())

def generate_nonce():
    return generate_random_string(NONCE_LENGTH)

def generate_signature(nonce, timestamp):
    parameter_dict = dict(PARAMETER_DICT)
    parameter_dict[OAUTH_NONCE_KEY] = nonce
    parameter_dict[OAUTH_TIMESTAMP_KEY] = timestamp

    parameter_keys = list(PARAMETER_KEYS)
    parameter_keys.sort()

    parameter_string = ''
    for parameter_key in parameter_keys:
        if len(parameter_string) > 0:
            parameter_string += '&'            
        parameter_string += parameter_key
        parameter_string += '='
        parameter_string += parameter_dict[parameter_key]
#    print(parameter_string)

#    print(parameter_string_encoded)

    signature_base_string = HTTP_METHOD
    signature_base_string += '&'
    signature_base_string += TWITTER_URL_PERCENT_ENCODED
    signature_base_string += '&'
    signature_base_string += urllib.parse.quote(parameter_string)
#    print(signature_base_string)

    oauth_signature = generate_base64_encoded_hmac_string(signature_base_string, SIGNING_KEY)
#    print(oauth_signature)

    return oauth_signature

def generate_curl_command():
    nonce = generate_nonce()
    timestamp = str(generate_timestamp())
    oauth_signature = generate_signature(nonce, timestamp)
    authorization_header = AUTHORIZATION_HEADER_TEMPLATE % (nonce, oauth_signature, timestamp)    
    curl_command_string = CURL_REQUEST_TEMPLATE % authorization_header
    print(curl_command_string)

def main():
    generate_curl_command()

### MAIN ###

if __name__ == '__main__':
    main()

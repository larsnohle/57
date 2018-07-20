#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import json
    
PORT = 9090
CURRENT_TIME = 'currentTime'

def ask_server_for_time():
    hostname = socket.gethostname()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hostname, PORT))
    received_bytes = client_socket.recv(4096)
    received_message_as_string = received_bytes.decode('utf-8')
    received_data_as_dict =json.loads(received_message_as_string)
    print("The current time is %s." % received_data_as_dict[CURRENT_TIME])

def main():
    ask_server_for_time()

### MAIN ###

if __name__ == '__main__':
    main()

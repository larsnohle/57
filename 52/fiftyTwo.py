#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import datetime
import json

TIMESTAMP_PATTERN = '{0:%Y-%m-%d %H:%M:%S}'
CURRENT_TIME = 'currentTime'
PORT = 9090

def create_time_data_to_send():
    current_time_as_string = TIMESTAMP_PATTERN.format(datetime.datetime.now())    
    d = dict()
    d[CURRENT_TIME] = current_time_as_string
    return json.dumps(d)

def send_string(client_socket, message_as_string):
    message_as_bytes = message_as_string.encode('utf-8')
    client_socket.send(message_as_bytes)

def start_server_socket():
    hostname = socket.gethostname()
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((hostname, PORT))
    serversocket.listen(5)

    while True:
        (client_socket, address) = serversocket.accept()
        print("Connection accepted!")
        send_string(client_socket, create_time_data_to_send())
        print("Message sent!")

def main():
    start_server_socket()

### MAIN ###

if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import datetime
import json
import random

PORT = 9090

QUOTES = ["Science is the belief in the ignorance of experts.", "The thing that doesn't fit is the thing that is most interesting.", "The first principle is that you must not fool yourself and you are the easiest person to fool", "Study hard what interests you the most in the most undisciplined, irreverent and original manner possible"]

def pick_quote():
    return QUOTES[random.randint(0, len(QUOTES) - 1)]

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
        send_string(client_socket, pick_quote())
        print("Message sent!")

def main():
    start_server_socket()

### MAIN ###

if __name__ == '__main__':
    main()

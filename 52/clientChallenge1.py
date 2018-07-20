#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

PORT = 9090

def ask_server_for_quote():
    hostname = socket.gethostname()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hostname, PORT))
    received_bytes = client_socket.recv(4096)
    received_message_as_string = received_bytes.decode('utf-8')
    print(received_message_as_string)

def main():
    ask_server_for_quote()

### MAIN ###

if __name__ == '__main__':
    main()

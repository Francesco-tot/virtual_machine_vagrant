#!/usr/bin/env python3
import socket
import sys


def client_program(h = socket.gethostname()):
    host = h  # as both code is running on same pc
    port = 5000  # socket server port number
    print(host)

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    if len(sys.argv) > 1:
        client_program(sys.argv[1])
    else:
        print("Usage: client.py <server_ip>")

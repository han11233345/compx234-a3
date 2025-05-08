import socket
import threading

tuple_space = {}

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024).decode('utf-8')

        if request.startswith('PUT'):

            _, k, v = request.split()

            if k in tuple_space:
                client_socket.send(f"ERR {k} already exists".encode('utf-8'))
            else:
                tuple_space[k] = v
                client_socket.send(f"OK {k} {v} added".encode('utf-8'))
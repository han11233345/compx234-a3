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

        elif request.startswith('GET'):
            _, k = request.split()
            if k in tuple_space:
                v = tuple_space.pop(k)
                client_socket.send(f"OK {k} {v} removed".encode('utf-8'))
            else:
                client_socket.send(f"ERR {k} does not exist".encode('utf-8'))

        elif request.startswith('DELETE'):
            _, k = request.split()
            if k in tuple_space:
                v = tuple_space.pop(k)
                client_socket.send(f"OK {k} {v} removed".encode('utf-8'))
            else:
                client_socket.send(f"ERR {k} does not exist".encode('utf-8'))

        elif request == 'EXIT':

              client_socket.close()
              break

    def start_server(host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
        print(f"Server started on {host}:{port}")
        while True:
            client_socket, addr = server.accept()
            print(f"Connection from {addr} established.")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    if __name__ == "__main__":
        start_server('localhost', 51234)



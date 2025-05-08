import socket
import sys


def client_request(host, port, request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

def process_file(host, port, file_name):
    with open(file_name, 'r') as file:
        for line in file:
            request = line.strip()
            client_request(host, port, request)

if __name__ == "__main__":
        host = sys.argv[1]
        port = int(sys.argv[2])
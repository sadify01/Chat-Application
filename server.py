import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

server_socket.bind((host, port))
server_socket.listen()

print(f"Server is listening on {host}:{port}")

clients = []

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        for client in clients:
            if client != client_socket:
                client.send(data)

    clients.remove(client_socket)
    client_socket.close()

while True:
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

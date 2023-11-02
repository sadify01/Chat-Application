import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 12345

client_socket.connect((host, port))

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode())

def receive_messages():
    while True:
        data = client_socket.recv(1024)
        print(data.decode())

send_thread = threading.Thread(target=send_messages)
receive_thread = threading.Thread(target=receive_messages)

send_thread.start()
receive_thread.start()

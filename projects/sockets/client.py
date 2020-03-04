import socket

cs = socket.socket()

cs.connect(('localhost', 9999))

name = input("Enter your name: ")
cs.send(bytes(name, 'utf-8'))

print(cs.recv(1024).decode())
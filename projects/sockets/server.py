import socket

ss = socket.socket()
print('Socket Created')

ss.bind(('localhost', 9999))

ss.listen(3)
print('Waiting for connections')

while True:
    cs, addr = ss.accept()
    name = cs.recv(1024).decode()
    print("Connected with", addr, name)

    cs.send(bytes("Welcome to Liopun", 'utf-8'))

    cs.close()
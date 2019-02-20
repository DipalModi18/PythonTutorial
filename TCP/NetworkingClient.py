import socket

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsock.connect(("127.0.0.1", 9999))

print("MSG: ", clientsock.recv(1024).decode('ascii'))

clientsock.close()

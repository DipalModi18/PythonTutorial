import socket

serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 9999
serversock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

data, addr = serversock.recvfrom(1024)
print("MSG: ", data.decode("ascii"))

serversock.close()

Docker
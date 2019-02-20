import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 9999
clientsocket.sendto("Hello server".encode("ascii"), (UDP_IP_ADDRESS, UDP_PORT_NO))

clientsocket.close()

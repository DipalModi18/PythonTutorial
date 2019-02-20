# Sockets are the endpoints of a bidirectional communications channel.
# Sockets may communicate within a process, between processes on the same machine,
#               or between processes on different continents.
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

host = socket.gethostname()
print("Host: ", host)

# bind(hostname, port)
serversocket.bind(("127.0.0.1", 9999))
print("Bind successfully")

serversocket.listen(5)
print("Listening...")

no = 0
while no < 3:
    clientsock, addr = serversocket.accept()
    print("Got a connection from: ", str(addr))
    clientsock.send(("Hello" + str(no)).encode("ascii"))
    no = no + 1
    clientsock.close()


serversocket.close()
print("Connection closed")

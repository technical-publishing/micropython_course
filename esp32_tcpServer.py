import socket
#IP-Adresse des ESP32-Servers
IP_ADR = '192.168.178.69'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello here is ESP32 TCP Server"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADR, TCP_PORT))
s.send (MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "Daten empfangen", data

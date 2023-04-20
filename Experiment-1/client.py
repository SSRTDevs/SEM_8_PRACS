import socket

# create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
sock.connect(('localhost', 3001))

# receive data from server
data = sock.recv(1024)

# print the received data
print(data.decode())

# send data to server
sock.send('I must have called a thousand times '.encode())

# close the connection
sock.close()
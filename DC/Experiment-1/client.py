import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(("localhost" , 3000))

data = clientSocket.recv(1024)

print(data.decode())

clientSocket.send("Message from client".encode())

clientSocket.close()
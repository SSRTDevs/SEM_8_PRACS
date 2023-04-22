import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(("localhost", 3000))

serverSocket.listen(1)

conn, addr = serverSocket.accept()

conn.send("From Server Side".encode())

data = conn.recv(1024)

print(data.decode())

serverSocket.close()
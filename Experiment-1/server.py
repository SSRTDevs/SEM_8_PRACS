import socket 

# This line creates a new socket object called sock, 
# using the socket.AF_INET address family (which uses IPv4 addressing) and the 
# socket.SOCK_STREAM socket type (which provides a reliable, stream-oriented connection).
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# This line binds the socket to a specific IP address and port number. 
# In this case, the IP address is 'localhost', which refers to the local machine, and the port number is 3001.
sock.bind(('localhost', 3001))


# This line tells the socket to start listening for incoming connections. 
# The 1 argument specifies the maximum number of queued connections that the socket can handle.
sock.listen(1)


# This line accepts an incoming connection from a client. 
# The accept() method blocks until a client connects, and 
# then returns a new socket object conn that the server can use to communicate with the client, and the client's address addr.
conn, addr = sock.accept()


# This line sends a message to the client over the connection. 
# The send() method sends a bytes-like object, 
# so we need to encode the string 'Hello, client!' as bytes using the encode() method.
conn.send('Hello, from the other side !'.encode())


# This line receives data from the client over the connection. 
# The recv() method blocks until it receives data, and 
# the 1024 argument specifies the maximum amount of data to receive at once.
data = conn.recv(1024)


# print the received data after decoding it from bytes
print(data.decode())


# close the connection
conn.close()
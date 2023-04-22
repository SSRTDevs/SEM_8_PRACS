import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.clients = []
    
    def listen(self):
        self.socket.listen()
        print(f"Server is listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.socket.accept()
            print(f"New client connected: {client_address}")
            self.clients.append(client_socket)
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()
    
    def handle_client(self, client_socket):
        while True:
            message = client_socket.recv(1024)
            for client in self.clients:
                if client != client_socket:
                    client.sendall(message)
                

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.socket.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")
    
    def send_message(self, message):
        self.socket.sendall(message.encode("utf-8"))
    
    def receive_messages(self):
        while True:
            message = self.socket.recv(1024).decode("utf-8")
            print(message)

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    
    server = Server(host, port)
    thread = threading.Thread(target=server.listen)
    thread.start()
    
    client1 = Client(host, port)
    client1.connect()
    client2 = Client(host, port)
    client2.connect()
    
    thread = threading.Thread(target=client1.receive_messages)
    thread.start()
    
    thread = threading.Thread(target=client2.receive_messages)
    thread.start()
    
    client1.send_message("Hello from client 1")
    client2.send_message("Hello from client 2")

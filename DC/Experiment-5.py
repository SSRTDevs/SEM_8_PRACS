import time

class Server:
    def __init__(self, id, coordinator_id, is_coordinator):
        self.id = id
        self.coordinator_id = coordinator_id
        self.is_coordinator = is_coordinator
        self.servers = []
        
    def add_server(self, server):
        self.servers.append(server)
        
    def start_election(self):
        for server in self.servers:
            if server.id > self.id:
                print(f"Server {self.id} sending 'Election' message to server {server.id}")
                server.receive_election(self.id)
                
        self.coordinator_id = self.id
        for server in self.servers:
            if server.id != self.id and server.id > self.coordinator_id:
                print(f"Server {self.id} sending 'Coordinator' message to server {server.id}")
                server.receive_coordinator(self.id)
                self.coordinator_id = server.id
                
        if self.coordinator_id == self.id:
            self.is_coordinator = True
            print(f"Server {self.id} is the new coordinator!")
        else:
            self.is_coordinator = False
        
    def receive_election(self, candidate_id):
        print(f"Server {self.id} received 'Election' message from server {candidate_id}")
        time.sleep(2)
        for server in self.servers:
            if server.id > self.id:
                print(f"Server {self.id} forwarding 'Election' message to server {server.id}")
                server.receive_election(candidate_id)
                
        self.coordinator_id = candidate_id
                
        print(f"Server {self.id} sending 'Coordinator' message to server {candidate_id}")
        candidate_server = next(server for server in self.servers if server.id == candidate_id)
        candidate_server.receive_coordinator(self.id)
    
    def receive_coordinator(self, coordinator_id):
        print(f"Server {self.id} received 'Coordinator' message from server {coordinator_id}")
        self.coordinator_id = coordinator_id
        self.is_coordinator = False


# Create servers
server1 = Server(1, None, False)
server2 = Server(2, None, False)
server3 = Server(3, None, False)
server4 = Server(4, None, False)
server5 = Server(5, None, False)

servers = [server1,server2,server3,server4,server5]
# Add servers to each other's lists of servers
for i in range(len(servers)):
    for j in range(len(servers)):
        if i != j:
            servers[i].add_server(servers[j])

# Start an election on server 5
print("Starting an election on server 3")
server3.start_election()

# Print the new coordinator
print(f"The new coordinator is {server3.coordinator_id}")





'''
class Server:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.coordinator_id = -1
        self.servers = []

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', self.port))
        self.socket.listen(1)
        print(f"Server {self.id} started, listening on port {self.port}")
        while True:
            conn, addr = self.socket.accept()
            print(f"Server {self.id}'s adress is {addr}")
            t = threading.Thread(target=self.handle_client, args=(self.id, conn, addr))
            t.start()

    def handle_client(self, id, conn, addr):
        data = conn.recv(1024).decode()
        print(data)
        if data == 'ELECTION':
            print(f"Received ELECTION from server {addr}")
            self.send_message_to_higher_servers(f"ELECTION {self.id}")
        elif data.startswith('ELECTOK'):
            print(f"Received ELECTOK from server {addr}")
            self.coordinator_id = int(data.split()[1])
            self.send_message_to_lower_servers(f"COORDINATOR {self.coordinator_id}")
        elif data == 'COORDINATOR':
            print(f"Received COORDINATOR from server {addr}")
            self.coordinator_id = self.id
            self.send_message_to_all_servers("OK")

    def send_message(self, host, port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(message.encode())

    def send_message_to_higher_servers(self, message):
        for s in self.servers:
            if s.id > self.id:
                self.send_message('localhost', s.port, message)

    def send_message_to_lower_servers(self, message):
        for s in self.servers:
            if s.id < self.id:
                self.send_message('localhost', s.port, message)

    def send_message_to_all_servers(self, message):
        for s.id in self.servers:
            self.send_message('localhost', s.port, message)

    def start_election(self):
        self.coordinator_id = -1
        self.send_message_to_higher_servers(f"ELECTION {self.id}")
        time.sleep(5)
        if self.coordinator_id == -1:
            self.coordinator_id = self.id
            self.send_message_to_all_servers(f"COORDINATOR {self.coordinator_id}")

if __name__ == '__main__':
    servers = [Server(1, 3001), Server(2, 3002), Server(3, 3003), Server(4,3004)]
    for i, s in enumerate(servers):
        s.servers = servers[i+1:]
        t = threading.Thread(target=s.start)
        t.start()
        time.sleep(2)
    time.sleep(5)
    servers[1].start_election()

'''
# This code simulates a simple network of 5 servers, each running on a separate thread. The `Server` class defines the behavior of each server. The `start` method initializes the server socket and listens for incoming connections. The `handle_client` method handles incoming messages from other servers.

# The `send_message` method sends a message to a specific host and port. The `send_message_to_higher_servers` method sends a message to all servers with a higher ID. The `send_message_to_lower_servers` method sends a message to all servers with a lower ID. The `send_message_to_all_servers` method sends a message to all servers.

# The `start_election` method starts

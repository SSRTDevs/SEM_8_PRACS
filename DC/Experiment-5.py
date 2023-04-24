import random

class Cluster:
    def __init__(self, num_servers):
        self.coordinator = -1
        self.num_servers = num_servers
        self.servers = [i for i in range(num_servers)]

    def start_election(self, node):
        for i in range(self.num_servers):
            if(i > node):
                print(f"Server {node} is sending election message to Server {i}")
        
        for i in range(self.num_servers):
            if(i > node):
                self.coordinator = self.start_election(i)
        
        if(self.coordinator!=-1 and node < self.coordinator):
            print(f"Server {self.coordinator} is sending coordinator message to Server {node}")
        
        return node
    
cluster = Cluster(6)
start_server = random.randint(0 , cluster.num_servers - 1)
print(f"Server {start_server} started the election process...")
cluster.start_election(start_server)

print(f"Now the coordinator is {cluster.coordinator}")

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

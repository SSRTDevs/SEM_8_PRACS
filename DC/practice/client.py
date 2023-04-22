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
cluster.start_election(start_server)

print(f"Now the coordinator is {cluster.coordinator}")
import itertools

# This is round robin based but we can also implement Least Connection,IP Hash, Weighted Round Robin, Least Response Time, Content-based
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_server(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

servers = ['Server1', 'Server2', 'Server3', 'Server4', 'Server5']
lb = LoadBalancer(servers)

# Simulate incoming requests
requests = range(1, 11)
for request in requests:
    server = lb.get_server()
    print(f"Request {request} is handled by {server}")

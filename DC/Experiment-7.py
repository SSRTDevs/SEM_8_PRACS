import threading
import time

class Node(threading.Thread):
    def __init__(self, node_id, num_nodes):
        super().__init__()
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.ack_count = 0
        self.requesting = False
        self.request_time = 0
        self.reply_time = 0
        self.reply_queue = []
        
    def run(self):
        time.sleep(1)
        self.request()
        
    def request(self):
        self.request_time = time.monotonic()
        self.requesting = True
        print(f"Node {self.node_id}: requesting critical section...")
        for i in range(self.num_nodes):
            if i == self.node_id:
                continue
            reply = self.send_request(i)
            if reply:
                self.ack_count += 1
        if self.ack_count == self.num_nodes - 1:
            self.enter_critical_section()
        else:
            self.reply_queue = []
        self.requesting = False
        self.ack_count = 0
            
    def send_request(self, node_id):
        print(f"Node {self.node_id}: sending request to Node {node_id}")
        node = nodes[node_id]
        if node.requesting and self.request_time < node.request_time:
            return False
        if node.requesting or node.reply_time > self.request_time:
            node.reply_queue.append(self.node_id)
            return False
        node.reply_time = time.monotonic()
        node.reply_queue.append(self.node_id)
        return True
    
    def enter_critical_section(self):
        print(f"Node {self.node_id}: entered critical section.")
        time.sleep(3)
        self.exit_critical_section()
        
    def exit_critical_section(self):
        print(f"Node {self.node_id}: exited critical section.")
        for node_id in self.reply_queue:
            self.send_reply(node_id)
        self.reply_queue = []
        
    def send_reply(self, node_id):
        print(f"Node {self.node_id}: sending reply to Node {node_id}")
        nodes[node_id].ack_count += 1
    
num_nodes = 5
nodes = [Node(i, num_nodes) for i in range(num_nodes)]
for node in nodes:
    node.start()
for node in nodes:
    node.join()

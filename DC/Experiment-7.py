# In this algorithm instead of using timestamps I am using priority numbers 
import threading
import time
import random

class Request:
    def __init__(self, id, priority):
        self.process_id = id
        self.priority = priority
        self.ack_cnt = set()

    def acknowledged(self, id):
        self.ack_cnt.add(id)

class Node(threading.Thread):
    def __init__(self, id, num_nodes, priority, requesting):
        super().__init__()
        self.id, self.num_nodes, self.priority, self.requesting = id, num_nodes, priority, requesting
        self.reply_queue, self.request = [], Request(id, priority)

    # Threading class function which has been overriden here 
    def run(self):
        time.sleep(1)
        if self.requesting: self.request_critical_section()

    def can_access_critical_section(self):
        return len(self.request.ack_cnt) == self.num_nodes - 1

    def request_critical_section(self):
        print(f"Node {self.id}: requesting critical section...")
        for i in range(self.num_nodes):
            if i == self.id: continue
            if not self.send_request(i): return
            self.request.acknowledged(i)
        if self.can_access_critical_section(): self.enter_critical_section()
    
    def send_request(self, id):
        node = nodes[id]
        if node.requesting and self.priority < node.priority:
            node.reply_queue.append(self.id)
            return False
        return True

    def enter_critical_section(self):
        print(f"Node {self.id}: entered critical section.")
        time.sleep(3)
        self.exit_critical_section()

    def exit_critical_section(self):
        print(f"Node {self.id}: exited critical section.")
        self.requesting = False
        for i in self.reply_queue:
            nodes[i].request.acknowledged(self.id)
            if nodes[i].can_access_critical_section(): nodes[i].enter_critical_section()
        self.reply_queue = []

num_nodes = 5
priorities = random.sample(range(1, num_nodes + 1), num_nodes)
requesting = [random.choice([True, False]) for _ in range(num_nodes)]
nodes = [Node(i, num_nodes, priorities[i], requesting[i]) for i in range(num_nodes)]

# Since Node class extends Threading we can directly use functions like start and join with each instance 
for node in nodes: node.start()

# Wait for all threads to finish
for node in nodes: node.join()
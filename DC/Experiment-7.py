import threading
import time

# In this algorithm instead of using timestamps I am using priority numbers 
class Node(threading.Thread):
    def __init__(self, node_id, num_nodes, priority, requesting):
        super().__init__()
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.ack_count = 0
        self.priority = priority
        self.requesting = requesting
        self.reply_queue = []
        
    # Threading class function which has been overriden here 
    def run(self):
        time.sleep(1)
        self.request()
        
    def request(self):
        if not self.requesting : 
            # process does not want to enter crtitical section 
            return
        
        print(f"Node {self.node_id}: requesting critical section...")
        for i in range(self.num_nodes):
            if i == self.node_id:
                continue
            reply = self.send_request(i)
            if reply:
                self.ack_count += 1
        if self.ack_count == self.num_nodes - 1:
            self.enter_critical_section()

        # I am in doubt here , if we should refresh the acknowledgement count or not ? 
        self.ack_count = 0
            
    def send_request(self, node_id):
        print(f"Node {self.node_id}: sending request to Node {node_id}")
        node = nodes[node_id]
        if node.requesting and self.priority < node.priority:
            node.reply_queue.append(self.node_id)
            return False
        return True
    
    def enter_critical_section(self):
        print(f"Node {self.node_id}: entered critical section.")
        time.sleep(3)
        self.exit_critical_section()
        
    def exit_critical_section(self):
        print(f"Node {self.node_id}: exited critical section.")
        self.requesting = False 
        for node_id in self.reply_queue:
            self.send_reply(node_id)
        self.reply_queue = []
        
    def send_reply(self, node_id):
        print(f"Node {self.node_id}: sending reply to Node {node_id}")
        nodes[node_id].request() ; 
    
num_nodes = 5
nodes = [Node(0, num_nodes, 2, True), Node(1, num_nodes, 4, False), Node(2, num_nodes, 3, False), Node(3, num_nodes, 5, False), Node(4, num_nodes, 1, True)]

# Since Node class extends Threading we can directly use functions like start and join with each instance 
for node in nodes:
    node.start()
for node in nodes:
    node.join()

# Explaining the output is bit difficult though
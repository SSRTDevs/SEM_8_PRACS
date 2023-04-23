from threading import Thread, Lock
import time

class RaymondTree:
    def __init__(self, num_nodes, node_id):
        self.num_nodes = num_nodes
        self.node_id = node_id
        self.requesting = False
        self.using = False
        self.pending_replies = 0
        self.child_nodes = []
        self.parent_node = None
        self.cs_enter_time = 0
        self.mutex = Lock()

    def set_parent(self, parent_id):
        self.parent_node = parent_id

    def add_child(self, child_id):
        self.child_nodes.append(child_id)

    def request_cs(self):
        self.mutex.acquire()
        self.requesting = True
        self.cs_enter_time = time.time()
        self.mutex.release()
        
        for child in self.child_nodes:
            send_request_msg(child, self.node_id, self.cs_enter_time)
        while self.pending_replies < len(self.child_nodes):
            time.sleep(0.1)
        
        self.mutex.acquire()
        self.using = True
        self.requesting = False
        self.mutex.release()

    def release_cs(self):
        self.mutex.acquire()
        self.using = False
        self.mutex.release()
        
        for child in self.child_nodes:
            send_release_msg(child, self.node_id)
        self.pending_replies = 0

    def handle_request(self, sender_id, timestamp):
        self.mutex.acquire()
        if self.using or (self.requesting and (timestamp, sender_id) < (self.cs_enter_time, self.node_id)):
            send_reply_msg(sender_id, self.node_id)
        else:
            self.pending_replies += 1
        self.mutex.release()

def send_request_msg(receiver_id, sender_id, timestamp):
    print(f"Node {sender_id} sending request to Node {receiver_id} at time {timestamp}")
    nodes[receiver_id].handle_request(sender_id, timestamp)

def send_reply_msg(receiver_id, sender_id):
    print(f"Node {sender_id} sending reply to Node {receiver_id}")
    nodes[receiver_id].pending_replies += 1

def send_release_msg(receiver_id, sender_id):
    print(f"Node {sender_id} sending release to Node {receiver_id}")
    nodes[receiver_id].handle_release(sender_id)

def run_algorithm(node_id):
    global nodes
    nodes = [RaymondTree(num_nodes, i) for i in range(num_nodes)]
    nodes[0].set_parent(None)
    nodes[0].add_child(1)
    nodes[0].add_child(2)
    nodes[1].set_parent(0)
    nodes[1].add_child(3)
    nodes[1].add_child(4)
    nodes[2].set_parent(0)
    nodes[2].add_child(5)
    nodes[2].add_child(6)
    nodes[3].set_parent(1)
    nodes[3].add_child(7)
    nodes[4].set_parent(1)
    nodes[4].add_child(8)
    nodes[5].set_parent(2)
    nodes[5].add_child(9)
    nodes[6].set_parent(2)
    nodes[6].add_child(10)

    nodes[node_id].request_cs()
    time.sleep(2)
    nodes[node_id].release_cs()

if __name__ == '__main__':
    num_nodes = 11
    threads = []
    for i in range(num_nodes):
        t = Thread(target=run_algorithm, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

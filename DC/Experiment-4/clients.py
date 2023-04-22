import socket 
import random
import time
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 3000))

while True : 

    data = sock.recv(1024).decode()
    print(data)
   
    nodes_time = [random.randint(1,10) for _ in range(0,4)]
    print(f"Clocks now: {nodes_time}")

    sock.send(json.dumps(nodes_time).encode())

    time.sleep(2)
    data = json.loads(sock.recv(1024).decode())
    print(f"Time corrections: {data}")

    nodes_time = [nodes_time[i] + data[i] for i in range(0,len(data))]
    print(f"Clocks after: {nodes_time}")
    time.sleep(10)
    print()

    


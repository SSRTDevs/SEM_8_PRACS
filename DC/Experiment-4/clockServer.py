import time 
import socket 
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 3000))

sock.listen(1)

conn, addr = sock.accept()

global_time = 10 
nodes = 5 
server_time = 10

while True : 
    time.sleep(5)
    global_time += 5 
    conn.send("Message from server: Send your timestamps...".encode())
    time.sleep(2)

    data = json.loads(conn.recv(1024).decode())
    data.append(server_time)

    print(f"Clocks recieved: {data}")
    print("Calculating average time differences of all the nodes")
    
    time_differences = [global_time-x for x in data]
    average = sum(time_differences) // nodes

    adjusted_time = [average - x for x in data]
    
    server_time += adjusted_time[-1]
    adjusted_time.pop()

    print("Sending time corrections...")
    conn.send(json.dumps(adjusted_time).encode())
    print()


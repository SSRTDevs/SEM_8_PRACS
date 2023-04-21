# Berkeley algorithm for time synchronization between distributed systems

import socket
import struct
import time

# Set up a UDP socket for time synchronization
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the Berkeley algorithm function
def berkeley_algorithm(time_diffs):
    # Compute the average time difference
    avg_time_diff = sum(time_diffs) / len(time_diffs)

    # Synchronize all clocks to the average time difference
    for i in range(len(time_diffs)):
        time_diffs[i] -= avg_time_diff

    return time_diffs

# Define the IP addresses and port numbers of the machines
machine_ips = ['192.168.100.12']
machine_ports = [5000]

# Define the number of iterations to run the algorithm for
num_iterations = 5

# Define the time difference array for each machine
time_diffs = [0] * len(machine_ips)

# Loop through the iterations
for i in range(num_iterations):
    # Get the time from each machine
    for j in range(len(machine_ips)):
        # Send a request for the current time to the machine
        sock.sendto('get_time'.encode(), (machine_ips[j], machine_ports[j]))

        # Receive the response from the machine
        data, addr = sock.recvfrom(1024)

        # Get the current time from the response
        current_time = struct.unpack('d', data)[0]

        # Compute the time difference between the current time and the local time
        time_diffs[j] = current_time - time.time()

    # Run the Berkeley algorithm to synchronize the clocks
    time_diffs = berkeley_algorithm(time_diffs)

    # Adjust the local time by the time difference
    local_time = time.time() + time_diffs[0]

    # Print the current iteration number and the local time
    print(f"Iteration {i+1}: Local time is {local_time}")

    # Wait for a short time before starting the next iteration
    time.sleep(1)

# Close the socket
sock.close()

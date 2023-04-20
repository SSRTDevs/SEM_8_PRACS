'''
Group communication typically involves multiple processes or nodes communicating
with each other simultaneously. One way to implement group communication is by 
using multicast sockets, which allow messages to be sent to a group of recipients at once.
The multicast address 224.0.0.0 to 239.255.255.255 is the range of addresses reserved for multicast use.
This address is not assigned to any particular organization or service, and it is not likely to be used by other applications.
'''

import socket
import struct 

# Set up the multicast address and port
multicast_group = ('224.3.29.71', 10000)

# Create a UDP socket and bind it to the local address
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 0))

# Set the time-to-live (TTL) for multicast packets
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

message = "Hey Bhai"
sock.sendto(message.encode(), multicast_group)

while True:

    # Send a message to the multicast group
    

    # Receive messages sent to the multicast group
    data, address = sock.recvfrom(1024)
    print(f'Received {data.decode()} from {address}')
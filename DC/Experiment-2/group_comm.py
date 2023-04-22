import socket
import struct

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Set the time-to-live (TTL) for multicast packets (Last Argument). TLL : Max number of hops before it is discarded.
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

# Tell the operating system to add the socket to the multicast group
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive messages sent to the multicast group
while True:
    data, address = sock.recvfrom(1024)
    print(f'Received {data.decode()} from {address}')

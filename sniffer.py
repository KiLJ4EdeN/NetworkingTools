import socket
import os
import datetime

# Listen on the service host.
host = "192.168.12.2"

# Create a Raw Socket and Bind It to The Public Interface
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    # Internet Control Message Protocol.
    socket_protocol = socket.IPPROTO_ICMP

# AF_INET: type of sockets with can communicate with. ipv4
# AF_INET6 for ipv6
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# Include IP Headers In the Capture.
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# If we're on Windows we need to send an IOCTL
# To setup promiscuous mode
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print(f'[INFO]: Sniffing on {host}...')
while True:
    # Read In A Single Packet.
    print(sniffer.recvfrom(65535))
    print(f'[INFO]: Packet:')
    print(f'[INFO]: {str(datetime.datetime.now())[0:19]}')

    # if we're on Windows turn off promiscuous mode
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

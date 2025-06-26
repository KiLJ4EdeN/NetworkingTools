import socket

# target_host = "www.google.com"
# target_port = 80
target_host = '0.0.0.0'
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

# client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
client.send(b"League of Legends")

response = client.recv(4096)

print(response.decode())

client.close()

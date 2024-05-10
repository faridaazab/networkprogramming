    ##1 import the socket library
from socket import *
    ##2 give the server IP and port number to make  the client can connect on it 
host = "127.0.0.1"
port = 2177
    ##3 create socket work on  IPV4 & tcp protocol 
         ##if i need IPV6 & UDP protocol write this client_server= socket(AF_UNIX,SOCK_DGRAM)
client_socket = socket(AF_INET, SOCK_STREAM)
    ##4 connect the server 
client_socket.connect((host, port))
print("Connected to the server.")

         ## Define buffer size as None initially
buffer_size = None
    ##5 infinite loop 
while True:
    sent_data = input("Client:")
    if sent_data.lower() == 'bye':
        client_socket.send(sent_data.encode("utf-8"))
        break
    client_socket.send(sent_data.encode("utf-8"))

         ## Receive data in chunks until no more data is received
    recv_data = b""
    while True:
         ## Use 4096 as default buffer size
        chunk = client_socket.recv(buffer_size or 4096)  
        if not chunk:
            break
        recv_data += chunk

    recv_data = recv_data.decode("utf-8")
    if recv_data.lower() == 'bye':
        break
    print("Server:", recv_data)

client_socket.close()

    ##1 import the socket library 
from socket import *
    ##2 define the server IP and port number  
host="127.0.0.1"
port=2177
    ##3 create socket work on  IPV4 & tcp protocol 
         ##if i need IPV6 & UDP protocol write this client_server= socket(AF_UNIX,SOCK_DGRAM)
server_socket=socket(AF_INET,SOCK_STREAM)
    ##4 connect IP & port with socket
server_socket.bind((host,port))
    ##5 listen(5) 5--> refers to waiting list
server_socket.listen(5)
    ##6 make the server accept the client addr and socket 
client_addr, client_socket= server_socket.accept()
    ##same as client.py but if i begin the client.py with receive data i must begin in server.py with send data
while True:
    recv_data=server_socket.recv(2048).decode("utf-8")
    if not recv_data:
        break
    if recv_data.lower()=='bye':
        break
    print(f"client:{recv_data}")

    send_data=input("server:")
    if send_data.lower()=='bye':
        client_socket.send(send_data.encode("utf-8"))
        break
    client_socket.send(send_data.encode("utf-8"))
    server_socket.close()

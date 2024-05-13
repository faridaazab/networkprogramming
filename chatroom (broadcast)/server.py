##1 import all needed libraries 
from socket import *
from _thread import *
import threading
##2 define the server IP and port number
host="127.0.0.1"
port=2177
##3 create socket work on  IPV4 & tcp protocol 
    ##if i need IPV6 & UDP protocol write this client_server= socket(AF_UNIX,SOCK_DGRAM)
server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()
##4 list to get all session numbers that created between client and server
clients=[]
## function to send all msgs to all clients in the network except the current client 
def broadcast_msg(message, currentclient):
    for client in clients:
        if client!= currentclient:
            client.send(message.encode("utf-8"))
## make a function to receive data from any client
def recv_msg(client):
    while True:
        message=client.recv(2048).decode("utf=8")
        broadcast_msg(message,client)
 
while True:
    client_socket , client_addr = server_socket.accept()
    ## add all client sockets or session numbers to list that have been created 
    clients.append(client_socket)
    thread=threading.Thread(target=recv_msg ,args=clients)
    thread.start()
    server_socket.close()

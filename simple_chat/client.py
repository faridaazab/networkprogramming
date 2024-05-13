    ##1 import the socket library 
from socket import * 
    ##2 define the server IP and port number  
host = "127.0.0.1"
port = 2177
    ##3 create socket work on  IPV4 & tcp protocol 
         ##if i need IPV6 & UDP protocol write this client_server= socket(AF_UNIX,SOCK_DGRAM)
client_socket = socket(AF_INET, SOCK_STREAM)
    ##4 connect the server
client_socket.connect((host, port))
print("Connected to the server.")
    ##5 infinite loop  
while True:
    ##store the input data from client in sent_data
    sent_data = input("Client:")
    ##if the client send bye to server sent it then exit
    if sent_data.lower() == 'bye':
        client_socket.send(sent_data.encode("utf-8"))
        break
    ##else the client any message not bye send it to server
    client_socket.send(sent_data.encode("utf-8"))
    ## after sending the message from client , client waits the message from server 
    recv_data = client_socket.recv(2048).decode("utf-8")
    ## if the received message is bye break the loop 
    if recv_data.lower() == 'bye':
        break
    ## else print the received data 
    print("Server:", recv_data)
    ##6 close the connection between the client and the server 
client_socket.close()
##1 import all needed libraries
from socket import *
from _thread import *
import threading
##2 define the server IP and port number
host="127.0.0.1"
port=2177
##3 create socket work on  IPV4 & tcp protocol 
    ##if i need IPV6 & UDP protocol write this client_server= socket(AF_UNIX,SOCK_DGRAM)
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(host,port)
#### make a function to receive data from server
def recv_msg():
    while True:
        recv_data=client_socket.recv(2048).decode("utf=8")
        print(recv_data)
## creating a thread 
thread=threading.Thread(target=recv_msg)
thread.start()

while True:
    send_data=input("")
    client_socket.send(send_data.encode("utf-8"))
    client_socket.close()
##1 import all needed libraries 
from socket import *
from _thread import *
import threading
##2 define the server IP and port number
host="127.0.0.1"
port=2177
##3 create the client_socket 
client_socket=socket(AF_INET,SOCK_STREAM)
## create function for receiving data 
def recv_thread(client_socket):
    while True:
        recv_data=client_socket.recv(2048).decode("utf-8")
        if not recv_data:
           break
        if recv_data.lower()=='bye':
           break
        print(f"client:{recv_data}")

while True:
    thread=threading.Thread(target=recv_thread,args=(client_socket))
    thread.start()
    thread.join()
    while True:
        send_data=input("server:")
        if send_data.lower()=='bye':
           client_socket.send(send_data.encode("utf-8"))
           break
        client_socket.send(send_data.encode("utf-8"))
    client_socket.close()

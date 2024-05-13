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
##4 connect ip and poert with server_socket
server_socket.bind((host,port))
##5 make server_socket listen all requests 
server_socket.listen(5)

##6 make a function to receive data from the thread
def recv_thread(session_id):
    while True:
        recv_data=session_id.recv(2048).decode("utf_8")
        if not recv_data:
           break
        if recv_data.lower()=='bye':
           break
        print(f"client:{recv_data}")

##7 create the threads 
def client_thread(session_id):
    thread=threading.Thread(target=recv_thread,args=(session_id,))
    thread.start()
    while True:
        send_data=input("server:")
        if send_data.lower()=='bye':
          session_id.send(send_data.encode("utf-8"))
          break
        session_id.send(send_data.encode("utf-8"))
   thread.join()
##8
while True:
   session_id ,client_addr = server_socket.accept()
   print(f"connected to:{client_addr[0]}")
   start_new_thread(client_thread,(session_id,))
   server_socket.close()
   

from socket import *
import datetime

host="127.0.0.1"
port=1234

server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(1)

while True:
    client_socket ,client_addr=server_socket.accept()
    current_time=str(datetime.datetime.now())
    client_socket.sendall(current_time.encode("utf-8"))
    client_socket.close()
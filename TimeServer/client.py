from socket import *

host="127.0.0.1"
port=1234

client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect((host,port))

current_time =client_socket.recv(1024).decode("utf-8")
print(f'current time :{current_time}')

client_socket.close()

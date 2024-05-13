import socket
import threading

host = '127.0.0.1'
port = 2770

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print("Server listening on {}:{}".format(host, port))

clients = []
aliases = []

def broadcast_msg(msg,currentclient,alias):
    for client in clients:
        if client!=currentclient:
            client.send(f"{alias}: {msg}".encode())


def recv_msg(client_socket,client_addr):
    alias=client_socket.recv(100).decode()
    clients.append(client_socket)
    aliases.append(alias)
    while True:
        data =client_socket.recv(2048).decode()
        broadcast_msg(data,client_socket,alias)
def start_thread():
    while True:
        client_socket ,client_addr=server_socket.accept()
        thread=threading.Thread(target=recv_msg,args=(client_socket,client_addr))
        thread.start()

accept_thread=threading.Thread(target=start_thread)
accept_thread.start()

accept_thread.join()

server_socket.close()


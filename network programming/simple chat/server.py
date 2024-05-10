    ##1 import the socket library
from socket import *

try:
    ##2  reserve a port on your computer
    host = "127.0.0.1"
    port = 2177
    ##3 create socket work on  IPV4 & tcp protocol 
         ##if i need IPV6 & UDP protocol write this client_server= socket(AF_UNIX,SOCK_DGRAM)
    server_socket = socket(AF_INET, SOCK_STREAM)
    ##4 bind to the host IP address and port number
    server_socket.bind((host, port))
    ##5 put the server into listening mode
    server_socket.listen(5)
    print("Server listening on {}:{}".format(host, port))
    ##6 establisg connection with client
    client_socket, client_address = server_socket.accept()
    print("Connection to: ", client_address[0])
    
    ## Define buffer size as None initially
    buffer_size = None
    ##7 infinite loop 
    while True:
        recv_data = client_socket.recv(buffer_size or 4096).decode("utf-8")
        if not recv_data:
            break

        if recv_data.lower() == 'bye':
            break

        print(f"Client: {recv_data}")

        sent_data = input("Server: ")
        if sent_data.lower() == 'bye':
            client_socket.send(sent_data.encode("utf-8"))
            break

        client_socket.send(sent_data.encode("utf-8"))

    ##8 end the connection between server and client 
    server_socket.close()

except error:
    print(error)
except KeyboardInterrupt:
    print("\n\nServer stopped by user")
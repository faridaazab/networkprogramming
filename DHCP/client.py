import socket

def dhcp_client():
	server_ip = '127.0.0.1' 
	server_port = 2177
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
		client_socket.settimeout(5)
		client_socket.sendto(b"DHCP request", (server_ip, server_port))
		try:
			response, _ = client_socket.recvfrom(1024)
			print(f"Received response from DHCP server: {response.decode()}")
		except socket.timeout:
			print("No response from DHCP server.")

if __name__ == "__main__":
	dhcp_client()
	


	
	
import threading
import socket
import argparse

# Setup command-line argument parsing
parser = argparse.ArgumentParser(description="TCP/UDP server for peer-to-peer communication")
parser.add_argument('--key', type=int, help='Identifier of either TCP (0) or UDP (1) connection')
args = parser.parse_args()

# TCP Server settings
tcp_host = '127.0.0.1'  # The server's hostname or IP address
tcp_port = 59000        # The port used by the server for TCP connections
  
# UDP Server settings
udp_host = '127.0.0.1'
udp_port = 59001

# Function to handle TCP clients
def handle_tcp_client(client_socket, address):
    print(f"[*] Accepted TCP connection from {address[0]}:{address[1]}")
    # Implement your TCP client handling logic here
    
                    print(f"[*] Accepted TCP connection from {address[0]}:{address[1]}")
                    while True:
                        try:
                            message = client_socket.recv(1024).decode('utf-8')
                            if message.startswith('request_list'):
                                # Client requested list of other clients
                                send_list_of_clients(client_socket)
                            else:
                                # Broadcast the received message to all clients
                                broadcast(message.encode('utf-8'))
                        except:
                            # Handle client disconnection
                            index = clients.index(client_socket)
                            clients.remove(client_socket)
                            client_socket.close()
                            nickname = nicknames[index]
                            # Notify all clients about the disconnection
                            broadcast(f'{nickname} has left the chat room!'.encode('utf-8'))
                            nicknames.remove(nickname)
                            break

# Function to handle UDP clients
def handle_udp_client():
    print("[*] UDP server is listening")
    # Create a UDP socket
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind((udp_host, udp_port))
    while True:
        data, address = udp_server.recvfrom(1024)
        print(f"Received UDP data from {address[0]}:{address[1]}: {data.decode()}")

# Start TCP server thread
def start_tcp_server():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((tcp_host, tcp_port))
    tcp_server.listen(5)
    print(f"[*] TCP server listening on {tcp_host}:{tcp_port}")
    while True:
        client_socket, address = tcp_server.accept()
        client_thread = threading.Thread(target=handle_tcp_client, args=(client_socket, address))
        client_thread.start()

# Start UDP server thread
def start_udp_server():
    udp_thread = threading.Thread(target=handle_udp_client)
    udp_thread.start()

# Determine whether to start TCP or UDP server based on key argument
if args.key == 0:
    print('Starting TCP server')
    start_tcp_server()

elif args.key == 1:
    print('Starting UDP server')
    start_udp_server()
else:
    print('Invalid key argument. Please specify 0 for TCP or 1 for UDP.')

# def handle_udp_client(udp_socket):
#     print("[*] UDP server is listening")
#     while True:
#         data, address = udp_socket.recvfrom(1024)
#         print(f"Received UDP data from {address[0]}:{address[1]}: {data.decode()}")
#         udp_socket.sendto(data, address)


# # Create a TCP/IP socket for control and signaling
# if (args.key==0):
#     tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     tcp_server.bind((tcp_host, tcp_port))
#     tcp_server.listen()  # Listen for incoming connections

# #UDP server thread
# else:
#     udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     udp_server.bind((udp_host,udp_port))
#     print(f"[*] UDP server listening on {udp_host}:{udp_port}")




# clients = []  # List to keep track of connected clients
# nicknames = []  # List to keep track of clients' nicknames

# # Function to broadcast a message to all connected clients
# def broadcast(message):
#     for client in clients:
#         client.send(message)

# # Main function to accept and handle incoming client connections
# def receive():
#     if(key == 0):
#         while True:
#             print('UTP Server is running and listening ...')
#             client, address = tcp_server.accept()
#             print(f'Connection is established with {str(address)}')

#             # Request and store the client's nickname
#             client.send('nickname?'.encode('utf-8'))
#             nickname = client.recv(1024).decode('utf-8')
#             nicknames.append(nickname)
#             clients.append(client)

#             print(f'The nickname of this client is {nickname}')
#             # Announce the new connection to all clients
#             broadcast(f'{nickname} has connected to the chat room'.encode('utf-8'))
#             # Confirm connection to the newly connected client
#             client.send('you are now connected!'.encode('utf-8'))

#             # Start a new thread to handle the client's messages
            
#             thread = threading.Thread(target=handle_tcp_client, args=(client,))
#             thread.start()
#     else:
#          while True:
#             print('UDP Server is running and listening ...')
#             client, address = udp_server.accept()
#             print(f'Connection is established with {str(address)}')

#             # Request and store the client's nickname
#             client.send('nickname?'.encode('utf-8'))
#             nickname = client.recv(1024).decode('utf-8')
#             nicknames.append(nickname)
#             clients.append(client)

#             print(f'The nickname of this client is {nickname}')
#             # Announce the new connection to all clients
#             broadcast(f'{nickname} has connected to the peer-to-peer connection'.encode('utf-8'))
#             # Confirm connection to the newly connected client
#             client.send('you are now connected!'.encode('utf-8'))

#             # Start a new thread to handle the client's messages
#             thread = threading.Thread(target=handle_udp_client, args=(client,))
#             thread.start()

import threading
import socket
import argparse
import sys

# Setup command-line argument parsing
parser = argparse.ArgumentParser(description="TCP/UDP client for peer-to-peer communication")
parser.add_argument('key', type=int, help='Identifier of either TCP (0) or UDP (1) connection')
parser.add_argument('--server_ip', type=str, help='IP address of the server')
parser.add_argument('--port', type=int, help='Port number of the server')
args = parser.parse_args()

# Create TCP/IP socket for TCP connection
if args.key == 0:
    print('Connecting to a TCP server')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((args.server_ip, args.port))
    # Function to handle receiving messages from the server
    def receive():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                print(message)
            except:
                # Handle any errors
                print('Error!')
                client_socket.close()
                break

    # Function for the client to send messages to the server
    def send():
        while True:
            message = input('')
            if message == "request_list":
                # Special command to request list of connected clients
                client_socket.send("request_list".encode('utf-8'))
            else:
                # Send any other message typed by the user
                client_socket.send(f'{nickname}: {message}'.encode('utf-8'))

    # Prompt the user to choose an nickname
    nickname = input('Choose a nickname >>> ')

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()

else:
    # Create UDP socket for UDP connection 
    print('Connecting to a UDP server')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((args.server_ip,args.port))
    # Function to handle receiving messages from the server
    def receive():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                print(message)
            except:
                # Handle any errors
                print('Error!')
                client_socket.close()
                break

# Function for the client to send messages to the server
def send():
    while True:
        message = input('')
        if message == "request_list":
            # Special command to request list of connected clients
            client_socket.send("request_list".encode('utf-8'))
        else:
            # Send any other message typed by the user
            client_socket.send(f'{nickname}: {message}'.encode('utf-8'))

# Prompt the user to choose an nickname
nickname = input('Choose a nickname >>> ')

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()

    


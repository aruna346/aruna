# Import necessary modules
import socket
import json
import sys

# Function to send a message to a socket
def send_message(sock, message):
    try:
        sock.send(message.encode())
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        sys.exit(1)

# Function to start the client
def main():
    # Load configuration from 'config.json' file
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Create a socket and connect to Server 1
    server1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server1_socket.connect((config['server1_ip'], config['server1_port']))

    # Create a socket and connect to Server 2
    server2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2_socket.connect((config['server2_ip'], config['server2_port']))

    try:
        while True:
            # Prompt the user to input a message
            message = input("Send message to servers: ")
            
            # Send the message to Server 1 and Server 2
            send_message(server1_socket, message)
            send_message(server2_socket, message)

            # Check if the user wants to exit the chat
            if message.lower() == 'exit':
                break

    except KeyboardInterrupt:
        pass  # Handle keyboard interrupt gracefully

    finally:
        # Send exit messages to both servers
        send_message(server1_socket, "client exit from chatting")
        send_message(server2_socket, "client exit from chatting")

        # Close the client sockets when finished
        server1_socket.close()
        server2_socket.close()

if __name__ == '__main__':
    main()

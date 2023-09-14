# Import necessary modules
import socket
import json

# Function to start the server
def main():
    # Load configuration from 'config.json' file
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server socket to the specified IP address and port
    server_socket.bind((config['server1_ip'], config['server1_port']))

    # Start listening for incoming connections with a maximum backlog of 5
    server_socket.listen(5)

    # Print a message to indicate that the server is listening
    print("Server 1 listening...")

    # Accept an incoming connection from a client
    client_socket, _ = server_socket.accept()

    # Print a message to indicate that the server has connected to a client
    print("Connected to client")

    try:
        while True:
            # Receive a message from the client and decode it
            message = client_socket.recv(config['buffer_size']).decode()
            if not message:
                break
            print(f"Received msg from client: {message}")
    except KeyboardInterrupt:
        pass  # Handle keyboard interrupt gracefully
    finally:
        # Close the client socket and server socket when finished
        client_socket.close()
        server_socket.close()

if __name__ == '__main__':
    main()

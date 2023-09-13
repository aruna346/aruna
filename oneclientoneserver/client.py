# Import necessary modules
import socket
import json

# Function to load configuration from 'config.json' file
def load_config():
    with open('config.json', 'r') as file:
        data = json.load(file)
    return data

# Function to start the client
def start_client(host, port, buffer_size):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server using the specified host and port
        s.connect((host, port))
        while True:
            # Prompt the user for a message to send to the server
            message = input("Client: ")
            if message == "exit":
                break
            # Send the message to the server
            s.sendall(message.encode())
            # Receive and print the server's response
            data = s.recv(buffer_size)
            if not data:
                print("Server has disconnected.")
                break
            print(f"Server: {data.decode()}")

# Load configuration from 'config.json'
config = load_config()

if __name__ == "__main__":
    # Start the client using the configuration values
    start_client(config["server_ip"], config["port"], config["buffer_size"])

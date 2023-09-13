# Import necessary modules
import socket
import json

# Function to load configuration from 'config.json' file
def load_config():
    with open('config.json', 'r') as file:
        data = json.load(file)
    return data

# Function to start the server
def start_server(host, port, buffer_size):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the specified host and port
        s.bind((host, port))
        # Start listening for incoming connections
        s.listen()
        print(f'Server started on {host}:{port}. Waiting for connection...')
        # Accept a connection from a client
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # Receive data from the client
                data = conn.recv(buffer_size)
                if not data:
                    print("Client has disconnected.")
                    break
                print(f"Client: {data.decode()}")
                message = input("Server: ")
                if message == "exit":
                    break
                # Send a response back to the client
                conn.sendall(message.encode())

# Load configuration from 'config.json'
config = load_config()

if __name__ == "__main__":
    # Start the server using the configuration values
    start_server(config["server_ip"], config["port"], config["buffer_size"])

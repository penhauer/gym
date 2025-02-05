import socket

def start_server(host='0.0.0.0', port=9999):
    # Create a socket object (IPv4, TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    server_socket.listen(5)  # Allow up to 5 connections in queue

    print(f"Server listening on {host}:{port}")

    while True:
        try:
            # Accept incoming connection
            client_socket, address = server_socket.accept()
            print(f"Connection established with {address}")

            while True:
                # Receive up to 1024 bytes
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8', errors='ignore')}")
                
            client_socket.close()
            print(f"Connection with {address} closed")

        except KeyboardInterrupt:
            print("Server shutting down...")
            break

    server_socket.close()

if __name__ == "__main__":
    start_server()

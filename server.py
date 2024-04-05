import socket
import threading

def handle_client(client_socket, client_address):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Print received data and broadcast to all clients
            message = f"{client_address}: {data.decode('utf-8')}"
            print(message)
            broadcast(message, client_socket)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the client socket when the loop ends
        client_socket.close()
        print(f"Connection with {client_address} closed.")

def broadcast(message, sender_socket):
    # Send the message to all clients except the sender
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                # Remove disconnected client
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def start_server():
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server socket to a specific address and port
    server_socket.bind(('127.0.0.1', 5555))

    # Enable server to accept connections (up to 5 clients in the queue)
    server_socket.listen(5)
    print("Server listening on 127.0.0.1:5555")

    try:
        while True:
            # Accept a connection from a client
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            # Add the client socket to the list of clients
            clients.append(client_socket)

            # Create a thread to handle the client's communication
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()

    except KeyboardInterrupt:
        print("Server shutting down.")
        server_socket.close()

if __name__ == "__main__":
    clients = []
    start_server()



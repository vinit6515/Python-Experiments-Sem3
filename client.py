import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            # Receive and print the echoed message from the server
            data = client_socket.recv(1024)
            print(data.decode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the client socket when the loop ends
        client_socket.close()
        print("Client socket closed.")

def start_client():
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('127.0.0.1', 5555))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    try:
        while True:
            # Get user input and send it to the server
            message = input("You: ")
            client_socket.send(message.encode('utf-8'))

    except KeyboardInterrupt:
        print("Client shutting down.")
        client_socket.close()

if __name__ == "__main__":
    start_client()

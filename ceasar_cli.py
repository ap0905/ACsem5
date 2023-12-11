import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1234))

    message = input("Enter a message to send to the server: ")
    client_socket.sendall(message.encode())

    # Receive and print the encrypted message from the server
    encrypted_message = client_socket.recv(1024).decode()
    print(f"Encrypted message received from server: {encrypted_message}")

    client_socket.close()

if __name__ == "__main__":
    main()

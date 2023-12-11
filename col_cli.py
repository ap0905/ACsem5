import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    key = input("Enter the key: ")
    message = input("Enter the plaintext: ")

    client_socket.sendall(f"{key}|{message}".encode())

    encrypted_message = client_socket.recv(1024).decode()
    print(f"Encrypted message received from server: {encrypted_message}")

    client_socket.close()

if __name__ == "__main__":
    main()

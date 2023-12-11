import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = input("Enter message to send to the server: ")
    key = input(f"Enter key of length {len(message)}: ")

    if len(key) != len(message):
        print("Error: Key length must be the same as the message length.")
        client_socket.close()
        return

    data = f"{key}|{message}"
    client_socket.send(data.encode())

    encrypted_text = client_socket.recv(1024).decode()
    print(f"Encrypted Text received from server: {encrypted_text}")

    client_socket.close()

if __name__ == "__main__":
    main()

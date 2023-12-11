import socket

def caesar_cipher(text, shift):
    encrypted_message = ''.join(chr((ord(char) + shift - ord('A')) % 26 + ord('A')) if char.isupper() else
                                chr((ord(char) + shift - ord('a')) % 26 + ord('a')) if char.islower() else 
                                char for char in text)
    return encrypted_message

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(1)

    print("Waiting for a connection...")
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    shift = int(input("Enter the shift value for the Caesar cipher: "))

    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        encrypted_message = caesar_cipher(message, shift)
        print(f"Received: {message}")
        client_socket.sendall(encrypted_message.encode())
        decrypted_message = caesar_cipher(encrypted_message, -shift)
        print(f"Decrypted: {decrypted_message}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

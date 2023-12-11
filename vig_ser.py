import socket

def vigenere_encrypt(message, key):
    encrypted_text = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            case_offset = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) + shift - case_offset) % 26 + case_offset)
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            case_offset = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift - case_offset) % 26 + case_offset)
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Waiting for a connection...")
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        key, message = data.split('|')

        encrypted_message = vigenere_encrypt(message, key)
        print(f"Received: {message}")
        print(f"Encrypted: {encrypted_message}")

        decrypted_message = vigenere_decrypt(encrypted_message, key)
        print(f"Decrypted: {decrypted_message}")

        client_socket.sendall(encrypted_message.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

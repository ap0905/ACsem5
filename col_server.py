import socket
import math

def encryptMessage(msg, key):
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    return cipher

def decryptMessage(cipher, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    dec_cipher = [[None] * col for _ in range(row)]
    
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    
    msg = ''.join(''.join(row) for row in dec_cipher).rstrip('_')
    return msg

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

        encrypted_message = encryptMessage(message, key)
        print(f"Received: {message}")
        print(f"Encrypted: {encrypted_message}")

        decrypted_message = decryptMessage(encrypted_message, key)
        print(f"Decrypted: {decrypted_message}")
        client_socket.sendall(encrypted_message.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()

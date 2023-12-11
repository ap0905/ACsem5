keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]
decryptedVector = [[0] for i in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def decrypt(cipherMatrix):
    determinant = (keyMatrix[0][0] * (keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1]) -
                   keyMatrix[0][1] * (keyMatrix[1][0] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][0]) +
                   keyMatrix[0][2] * (keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0])) % 26

    if determinant == 0:
        print("The key is not invertible. Decryption is not possible.")
        return

    determinant_inv = pow(determinant, -1, 26)  # Computing modular inverse of determinant

    adjugate_matrix = [
        [(keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1]) % 26,
         (keyMatrix[0][2] * keyMatrix[2][1] - keyMatrix[0][1] * keyMatrix[2][2]) % 26,
         (keyMatrix[0][1] * keyMatrix[1][2] - keyMatrix[0][2] * keyMatrix[1][1]) % 26],

        [(keyMatrix[1][2] * keyMatrix[2][0] - keyMatrix[1][0] * keyMatrix[2][2]) % 26,
         (keyMatrix[0][0] * keyMatrix[2][2] - keyMatrix[0][2] * keyMatrix[2][0]) % 26,
         (keyMatrix[0][2] * keyMatrix[1][0] - keyMatrix[0][0] * keyMatrix[1][2]) % 26],

        [(keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0]) % 26,
         (keyMatrix[0][1] * keyMatrix[2][0] - keyMatrix[0][0] * keyMatrix[2][1]) % 26,
         (keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0]) % 26]
    ]

    inverse_keyMatrix = [[(element * determinant_inv) % 26 for element in row] for row in adjugate_matrix]

    for i in range(3):
        for j in range(1):
            decryptedVector[i][j] = 0
            for x in range(3):
                decryptedVector[i][j] += (inverse_keyMatrix[i][x] * cipherMatrix[x][j])
            decryptedVector[i][j] = decryptedVector[i][j] % 26

def HillCipher(message, key):
    getKeyMatrix(key)

    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    encrypt(messageVector)

    CipherText = ''.join(chr(cipherMatrix[i][0] + 65) for i in range(3))
    print("Ciphertext:", CipherText)

    decrypt(cipherMatrix)

    DecryptedText = ''.join(chr(decryptedVector[i][0] + 65) for i in range(3))
    print("Decrypted text:", DecryptedText)

def main():
    message = input("Enter the message (3 characters): ").upper()
    if len(message) != 3 or not message.isalpha():
        print("Invalid input. Please enter a valid 3-character alphabetic message.")
        return

    key = input("Enter the key (9 characters): ").upper()
    if len(key) != 9 or not key.isalpha():
        print("Invalid input. Please enter a valid 9-character alphabetic key.")
        return

    HillCipher(message, key)

if __name__ == "__main__":
    main()

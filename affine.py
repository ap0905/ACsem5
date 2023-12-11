import math

def modinv(a, m):
    return next((x for x in range(1, m) if (a * x) % m == 1), None)

def affine_encrypt(text, key):
    return ''.join(
        chr((key[0] * (ord(char.upper()) - ord('A')) + key[1]) % 26 + ord('A')).lower() if char.islower() else
        chr((key[0] * (ord(char) - ord('A')) + key[1]) % 26 + ord('A')) if char.isalpha() else char
        for char in text
    )

def affine_decrypt(text, key):
    modular_inverse = modinv(key[0], 26)
    if modular_inverse is None:
        return "Modular inverse does not exist for the given key."

    return ''.join(
        chr((modular_inverse * (ord(char.upper()) - ord('A') - key[1])) % 26 + ord('A')).lower() if char.islower() else
        chr((modular_inverse * (ord(char) - ord('A') - key[1])) % 26 + ord('A')) if char.isalpha() else char
        for char in text
    )

def main():
    text = input("Enter the plain text: ")
    a = int(input("Enter the 'a' key (an integer): "))
    b = int(input("Enter the 'b' key (an integer): "))
    key = [a, b]

    affine_encrypted_text = affine_encrypt(text, key)
    print('Encrypted Text:', affine_encrypted_text)

    decrypted_text = affine_decrypt(affine_encrypted_text, key)
    print('Decrypted Text:', decrypted_text)

if __name__ == '__main__':
    main()

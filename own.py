def replace_vowels(plain_text, direction):
    vowels = "aeiouAEIOU"
    encrypted_text = ""
    for char in plain_text:
        if char in vowels:
            index = vowels.index(char)
            next_vowel = vowels[(index + direction) % len(vowels)]
            encrypted_text += next_vowel
        else:
            encrypted_text += char
    return encrypted_text

def fixed_permutation(plain_text):
    permutation = [2, 1, 0, 3, 4]
    permuted_text = [plain_text[i] for i in permutation]
    return permuted_text, permutation

def encrypt(plain_text):
    print("Original text:", plain_text)

    # Step 1: Vowel Substitution
    substituted_text = replace_vowels(plain_text,1)
    print("After vowel substitution:", substituted_text)

    # Step 2: Fixed Permutation
    permuted_text, permutation = fixed_permutation(substituted_text)
    print("After fixed permutation:", permuted_text)

    cipher_text = ''.join(permuted_text)
    print("Encrypted text:", cipher_text)

    return cipher_text, permutation

def decrypt(cipher_text, permutation):
    print("Cipher text:", cipher_text)

    # Step 1: Reverse Permutation
    reversed_permutation = [permutation.index(i) for i in range(len(permutation))]
    permuted_text = [cipher_text[i] for i in reversed_permutation]
    print("After reversing permutation:", permuted_text)

    # Step 2: Vowel Substitution
    decrypted_text = replace_vowels(''.join(permuted_text), -1)
    print("After vowel substitution:", decrypted_text)

    return decrypted_text

# Example usage:
plain_text = input("Enter plain text: ")
cipher_text, permutation = encrypt(plain_text)
decrypted_text = decrypt(cipher_text, permutation)

print("Decrypted text:", decrypted_text)

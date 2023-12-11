def generate_public_key(private_key, q, r):
    if any(private_key[i] <= sum(private_key[:i]) for i in range(len(private_key))):
        raise ValueError("Input sequence is not super-increasing")

    return [(r * element) % q for element in private_key]

def knapsack_encrypt(plaintext, public_key):
    binary_message = [int(bit) for bit in plaintext]
    if len(binary_message) != len(public_key):
        raise ValueError("Length of the binary message must match the length of the public key")

    return sum(bit * key for bit, key in zip(binary_message, public_key))

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the super-increasing sequence (n): "))
    q = int(input("Enter the modulus (q): "))
    r = int(input("Enter the multiplier (r): "))

    # Input the super-increasing sequence
    private_key = [int(input(f"Enter element {i + 1} of the super-increasing sequence: ")) for i in range(n)]

    public_key = generate_public_key(private_key, q, r)

    print("Super-Increasing Sequence (Private Key):", private_key)
    print("Public Key:", public_key)

    plaintext = input("Enter the binary plaintext: ")
    ciphertext = knapsack_encrypt(plaintext, public_key)

    print("Original Message:", plaintext)
    print("Encrypted Ciphertext:", ciphertext)

import math

def modinv(e, phi):
    d = pow(e, -1, phi)
    return d

p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e = e + 1

d = modinv(e, phi)

# Display calculated values
print("Prime numbers (p and q):", p, q)
print("Product (n):", n)
print("Euler's totient (phi):", phi)
print("Public key (e, n):", e, n)
print("Private key (d, n):", d, n)

# Take input message
msg = int(input("Enter the message to encrypt: "))

print("Message data =", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e, n)  # Use pow with modulo for better performance
print("Encrypted data =", c)

# Decryption m = (c ^ d) % n
m = pow(c, d, n)  # Use pow with modulo for better performance
print("Original Message Sent =", m)

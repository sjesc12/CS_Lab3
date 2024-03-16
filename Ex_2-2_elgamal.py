import random
from math import gcd

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def generate_keys(p, g):
    # Choose a random private key
    private_key = random.randint(2, p - 2)
    
    # Calculate the public key
    public_key = mod_exp(g, private_key, p)
    
    return private_key, public_key

def encrypt(message, p, g, public_key):
    # Generate a random ephemeral key
    k = random.randint(2, p - 2)
    
    # Calculate the shared secret key
    shared_secret_key = mod_exp(public_key, k, p)
    
    # Encrypt the message
    ciphertext_part1 = mod_exp(g, k, p)
    ciphertext_part2 = (message * shared_secret_key) % p
    
    return ciphertext_part1, ciphertext_part2

def decrypt(ciphertext_part1, ciphertext_part2, private_key, p):
    # Calculate the shared secret key
    shared_secret_key = mod_exp(ciphertext_part1, private_key, p)
    
    # Decrypt the message
    message = (ciphertext_part2 * mod_exp(shared_secret_key, p - 2, p)) % p
    
    return message

# Input parameters
p = int(input("Enter the prime number (p): "))
g = int(input("Enter the generator (g): "))

# Generate keys
private_key, public_key = generate_keys(p, g)
print("Private Key:", private_key)
print("Public Key:", public_key)

# Encryption
message = int(input("Enter the message to encrypt: "))
ciphertext_part1, ciphertext_part2 = encrypt(message, p, g, public_key)
print("Ciphertext Part 1:", ciphertext_part1)
print("Ciphertext Part 2:", ciphertext_part2)

# Decryption
decrypted_message = decrypt(ciphertext_part1, ciphertext_part2, private_key, p)
print("Decrypted Message:", decrypted_message)

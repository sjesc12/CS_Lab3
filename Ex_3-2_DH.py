def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def diffie_hellman(p, g, a, b):
    # Alice's public key
    A = mod_exp(g, a, p)
    
    # Bob's public key
    B = mod_exp(g, b, p)

    # Shared secret key for Alice
    shared_secret_alice = mod_exp(B, a, p)
    
    # Shared secret key for Bob
    shared_secret_bob = mod_exp(A, b, p)
    
    return A, B, shared_secret_alice, shared_secret_bob

# Input parameters
p = int(input("Enter the prime number (p): "))
g = int(input("Enter the generator (g): "))
a = int(input("Enter Alice's private key (a): "))
b = int(input("Enter Bob's private key (b): "))

# Perform Diffie-Hellman key exchange
A, B, shared_secret_alice, shared_secret_bob = diffie_hellman(p, g, a, b)

# Print public keys and shared key
print("\nPublic Key for Alice (A):", A)
print("Public Key for Bob (B):", B)

# Verify if the shared secret keys match
if shared_secret_alice == shared_secret_bob:
    print("Shared secret keys match!")
    print("Shared Secret Key:", shared_secret_alice)
else:
    print("Error: Shared secret keys do not match!")

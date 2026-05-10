# =========================================================
# Task 1: Simple RSA Implementation (Without Libraries)
# =========================================================
# Objective:
# - Generate RSA keys manually using small prime numbers
# - Encrypt a message using public key
# - Decrypt a message using private key
# =========================================================
# Function to calculate GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None
# ---------------- RSA Key Generation ----------------
# Small prime numbers
p = 17
q = 11
# Step 1: Calculate n
n = p * q
# Step 2: Calculate Euler's Totient Function
phi = (p - 1) * (q - 1)
# Step 3: Choose e
e = 7
# Check if e and phi are coprime
if gcd(e, phi) != 1:
    print("e and phi are not coprime")
    exit()
# Step 4: Calculate d
d = mod_inverse(e, phi)
# Public and Private Keys
public_key = (e, n)
private_key = (d, n)
print("========== RSA KEY GENERATION ==========")
print("Prime numbers:")
print("p =", p)
print("q =", q)
print("\nCalculated values:")
print("n =", n)
print("phi =", phi)
print("\nPublic Key (e, n):", public_key)
print("Private Key (d, n):", private_key)
# ---------------- Encryption Function ----------------
def encrypt(message, public_key):
    e, n = public_key
    encrypted = []
    for char in message:
        # Convert character to ASCII
        m = ord(char)
        # RSA Encryption Formula: C = M^e mod n
        c = (m ** e) % n
        encrypted.append(c)
    return encrypted
# ---------------- Decryption Function ----------------
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted = ""
    for c in ciphertext:
        # RSA Decryption Formula: M = C^d mod n
        m = (c ** d) % n
        decrypted += chr(m)
    return decrypted
# ---------------- Test RSA ----------------
message = "ISMAIL"
print("\n========== RSA ENCRYPTION ==========")
print("Original Message:", message)
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, private_key)
print("\n========== RSA DECRYPTION ==========")
print("Decrypted Message:", decrypted_message)
# =========================================================
# Digital Signature using RSA + SHA256
# =========================================================
import hashlib
# ---------------- RSA KEY GENERATION ----------------
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None
# Small prime numbers
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17  # public exponent
d = mod_inverse(e, phi)
public_key = (e, n)
private_key = (d, n)
print("Public Key:", public_key)
print("Private Key:", private_key)
# ---------------- HASH FUNCTION ----------------
def create_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()
# ---------------- SIGN MESSAGE ----------------
def sign_message(message, private_key):
    d, n = private_key
    # Step 1: Hash the message
    message_hash = create_hash(message)
    # Step 2: Convert hash to integer
    hash_int = int(message_hash, 16)
    # Step 3: Sign using private key
    signature = pow(hash_int, d, n)
    return signature
# ---------------- VERIFY SIGNATURE ----------------
def verify_signature(message, signature, public_key):
    e, n = public_key
    # Hash the message again
    new_hash = create_hash(message)
    new_hash_int = int(new_hash, 16)
    # Decrypt signature using public key
    decrypted_hash = pow(signature, e, n)
    return (new_hash_int % n) == decrypted_hash
# ---------------- TEST CASES ----------------
message = "Hello RSA"
print("\nOriginal Message:", message)
# Sign
signature = sign_message(message, private_key)
print("Signature:", signature)
# Verify original
result1 = verify_signature(message, signature, public_key)
print("Verification (Original):", result1)
# Modify message
modified_message = "Hello rsa"
print("\nModified Message:", modified_message)
# Verify modified
result2 = verify_signature(modified_message, signature, public_key)
print("Verification (Modified):", result2)
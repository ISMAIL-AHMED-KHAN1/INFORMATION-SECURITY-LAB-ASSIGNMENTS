# Parameters for a small curve: y^2 = x^3 + 2x + 2 (mod 17)
P = 17
A = 2
B = 2
def point_addition(P1, P2, a, p):
    if P1 is None: return P2
    if P2 is None: return P1 
    x1, y1 = P1
    x2, y2 = P2
    if x1 == x2 and y1 != y2:
        return None  # Point at infinity
    if P1 == P2:
        # Point Doubling
        m = (3 * x1**2 + a) * pow(2 * y1, -1, p)
    else:
        # Standard Addition
        m = (y2 - y1) * pow(x2 - x1, -1, p)
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)
def multiply(P1, k, a, p):
    # Scalar multiplication: k * P
    result = None
    addend = P1
    for bit in bin(k)[2:][::-1]:
        if bit == '1':
            result = point_addition(result, addend, a, p)
        addend = point_addition(addend, addend, a, p)
    return result
# --- Key Generation ---
# Generator Point G
G = (5, 1) 
private_key = 3  # Chosen randomly
public_key = multiply(G, private_key, A, P)
print(f"ECC Key Pair Generated:\nPrivate Key: {private_key}\nPublic Key: {public_key}")
# --- Simple EC-ElGamal Encryption ---
msg_point = (9, 1) # A message mapped to a point on the curve
k_random = 2      # Random value for encryption
# Ciphertext (C1, C2)
c1 = multiply(G, k_random, A, P)
shared_secret = multiply(public_key, k_random, A, P)
c2 = point_addition(msg_point, shared_secret, A, P)
print(f"\nEncrypted Message Point: ({c1}, {c2})")
# --- Decryption ---
# Decryption: msg = C2 - (private_key * C1)
s = multiply(c1, private_key, A, P)
# Subtracting is adding the point with negative y
s_neg = (s[0], -s[1] % P)
decrypted_msg = point_addition(c2, s_neg, A, P)
print(f"Decrypted Message Point: {decrypted_msg}")
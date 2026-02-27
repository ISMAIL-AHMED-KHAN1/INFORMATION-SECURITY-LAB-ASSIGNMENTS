"""
Caesar Cipher Program
This program provides two functions:
1. caesar_encrypt(text, shift)  -> Encrypts a message
2. caesar_decrypt(ciphertext, shift) -> Decrypts a message

Only alphabetic characters are shifted.
Uppercase and lowercase letters are preserved.
Spaces and special characters remain unchanged.
"""
def caesar_encrypt(text, shift):
    """
    Encrypts the given text using Caesar Cipher.
    
    Parameters:
        text (str): The message to encrypt
        shift (int): Number of positions to shift each letter
        
    Returns:
        str: Encrypted message
    """ 
    encrypted_text = ""  # Store the final encrypted result
    
    for char in text:
        # Check if character is uppercase
        if char.isupper():
            # Convert letter to ASCII, shift, wrap using modulo, convert back to char
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
        # Check if character is lowercase
        elif char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        # If not a letter, keep it unchanged
        else:
            encrypted_text += char
    
    return encrypted_text
def caesar_decrypt(ciphertext, shift):
    """
    Decrypts a Caesar Cipher encrypted message.
    
    Parameters:
        ciphertext (str): The encrypted message
        shift (int): Number of positions originally shifted   
    Returns:
        str: Decrypted original message
    """ 
    # Decryption is just shifting backwards
    return caesar_encrypt(ciphertext, -shift)
# Example usage
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value: "))
    
    encrypted = caesar_encrypt(message, shift_value)
    print("Encrypted Message:", encrypted)
    
    decrypted = caesar_decrypt(encrypted, shift_value)
    print("Decrypted Message:", decrypted)
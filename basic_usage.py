"""
Basic Usage Examples for Caesar Cipher
Demonstrates how to use the caesar_cipher module
"""

from caesar_cipher import encrypt_message, decrypt_message, brute_force_decrypt

def main():
    print("Caesar Cipher - Basic Usage Examples")
    print("=" * 40)
    
    # Example 1: Simple encryption and decryption
    print("\n1. Basic Encryption/Decryption:")
    message = "Hello, World!"
    shift = 5
    
    encrypted = encrypt_message(message, shift)
    decrypted = decrypt_message(encrypted, shift)
    
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Example 2: Famous Caesar cipher example
    print("\n2. Historical Example (Julius Caesar used shift of 3):")
    historical_message = "The die is cast"
    caesar_shift = 3
    
    encrypted_historical = encrypt_message(historical_message, caesar_shift)
    print(f"Original:  {historical_message}")
    print(f"Encrypted: {encrypted_historical}")
    
    # Example 3: Handling edge cases
    print("\n3. Edge Cases:")
    edge_cases = [
        ("ABC", 25),  # Near end of alphabet
        ("XYZ", 3),   # Wraparound case
        ("Hello123!", 7),  # Mixed content
        ("", 5),      # Empty string
    ]
    
    for text, shift in edge_cases:
        encrypted = encrypt_message(text, shift)
        print(f"'{text}' with shift {shift} -> '{encrypted}'")
    
    # Example 4: Brute force demonstration
    print("\n4. Brute Force Attack Example:")
    secret_message = "WKLV LV D VHFUHW"
    print(f"Intercepted message: {secret_message}")
    print("Trying all possible shifts...")
    
    # Try all shifts and look for meaningful text
    for shift in range(1, 26):
        decrypted = decrypt_message(secret_message, shift)
        print(f"Shift {shift:2d}: {decrypted}")
        # Shift 3 should reveal: "THIS IS A SECRET"

if __name__ == "__main__":
    main()
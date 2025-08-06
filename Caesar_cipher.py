"""
Caesar Cipher Implementation
freeCodeCamp Scientific Computing with Python - Chapter 1

A Caesar cipher is a simple substitution cipher where each letter in the plaintext 
is shifted a certain number of places down or up the alphabet.

Author: [Your Name]
Date: August 2025
"""

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar cipher algorithm.
    
    Args:
        text (str): The text to encrypt or decrypt
        shift (int): The number of positions to shift each letter
        mode (str): 'encrypt' or 'decrypt' - determines direction of shift
    
    Returns:
        str: The encrypted or decrypted text
    
    Examples:
        >>> caesar_cipher("HELLO", 3, 'encrypt')
        'KHOOR'
        >>> caesar_cipher("KHOOR", 3, 'decrypt')
        'HELLO'
    """
    # Convert to uppercase for consistency
    text = text.upper()
    result = ""
    
    # Adjust shift direction for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Process each character
    for char in text:
        if char.isalpha():
            # Get position in alphabet (A=0, B=1, etc.)
            char_pos = ord(char) - ord('A')
            
            # Apply shift with wraparound using modulo
            new_pos = (char_pos + shift) % 26
            
            # Convert back to character
            new_char = chr(new_pos + ord('A'))
            result += new_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def encrypt_message(message, shift):
    """
    Convenience function to encrypt a message.
    
    Args:
        message (str): The message to encrypt
        shift (int): The shift value
    
    Returns:
        str: The encrypted message
    """
    return caesar_cipher(message, shift, 'encrypt')


def decrypt_message(message, shift):
    """
    Convenience function to decrypt a message.
    
    Args:
        message (str): The message to decrypt
        shift (int): The shift value
    
    Returns:
        str: The decrypted message
    """
    return caesar_cipher(message, shift, 'decrypt')


def brute_force_decrypt(encrypted_text):
    """
    Attempts to decrypt a message by trying all possible shift values.
    Useful when you don't know the shift value.
    
    Args:
        encrypted_text (str): The encrypted text to decrypt
    
    Returns:
        dict: Dictionary with shift values as keys and decrypted text as values
    """
    results = {}
    print("Brute force decryption attempts:")
    print("-" * 40)
    
    for shift in range(26):
        decrypted = decrypt_message(encrypted_text, shift)
        results[shift] = decrypted
        print(f"Shift {shift:2d}: {decrypted}")
    
    return results


def demonstrate_string_manipulation():
    """
    Demonstrates various string manipulation techniques used in the cipher.
    """
    print("=== String Manipulation Techniques Demo ===\n")
    
    # 1. String case conversion
    original = "Hello World!"
    print(f"1. Case Conversion:")
    print(f"   Original: {original}")
    print(f"   Upper:    {original.upper()}")
    print(f"   Lower:    {original.lower()}")
    print()
    
    # 2. Character iteration and checking
    print(f"2. Character Analysis:")
    for char in original[:5]:  # First 5 characters
        print(f"   '{char}' -> Is alpha: {char.isalpha()}, Is digit: {char.isdigit()}")
    print()
    
    # 3. ASCII values and chr/ord functions
    print(f"3. ASCII Values:")
    print(f"   ord('A') = {ord('A')}")
    print(f"   ord('Z') = {ord('Z')}")
    print(f"   chr(65) = '{chr(65)}'")
    print(f"   chr(90) = '{chr(90)}'")
    print()
    
    # 4. Modulo arithmetic for wraparound
    print(f"4. Modulo Arithmetic (Wraparound):")
    print(f"   (25 + 3) % 26 = {(25 + 3) % 26} (Z + 3 wraps to C)")
    print(f"   (2 - 5) % 26 = {(2 - 5) % 26} (C - 5 wraps to X)")
    print()


def interactive_cipher():
    """
    Interactive function to allow users to encrypt/decrypt messages.
    """
    print("=== Interactive Caesar Cipher ===")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute force decrypt")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            message = input("Enter message to encrypt: ")
            try:
                shift = int(input("Enter shift value (0-25): "))
                encrypted = encrypt_message(message, shift)
                print(f"Encrypted: {encrypted}")
            except ValueError:
                print("Please enter a valid number for shift value.")
                
        elif choice == '2':
            message = input("Enter message to decrypt: ")
            try:
                shift = int(input("Enter shift value (0-25): "))
                decrypted = decrypt_message(message, shift)
                print(f"Decrypted: {decrypted}")
            except ValueError:
                print("Please enter a valid number for shift value.")
                
        elif choice == '3':
            message = input("Enter encrypted message: ")
            brute_force_decrypt(message)
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")


def run_tests():
    """
    Runs a series of tests to verify the cipher implementation.
    """
    print("=== Running Tests ===\n")
    
    test_cases = [
        ("HELLO", 3, "KHOOR"),
        ("WORLD", 5, "BTWQI"),
        ("PYTHON", 13, "CLGUBA"),
        ("ABC", 25, "ZAB"),
        ("XYZ", 3, "ABC"),
        ("Hello, World! 123", 7, "OLSSV, DVYSK! 123")
    ]
    
    all_passed = True
    
    for i, (text, shift, expected) in enumerate(test_cases, 1):
        encrypted = encrypt_message(text, shift)
        decrypted = decrypt_message(encrypted, shift)
        
        print(f"Test {i}:")
        print(f"  Input: '{text}' (shift {shift})")
        print(f"  Encrypted: '{encrypted}'")
        print(f"  Expected:  '{expected}'")
        print(f"  Decrypted: '{decrypted}'")
        
        if encrypted == expected and decrypted.upper() == text.upper():
            print("  ✓ PASSED")
        else:
            print("  ✗ FAILED")
            all_passed = False
        print()
    
    if all_passed:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed.")


def main():
    """
    Main function demonstrating the Caesar cipher functionality.
    """
    print("Caesar Cipher - Scientific Computing with Python")
    print("=" * 50)
    
    # Demonstrate string manipulation techniques
    demonstrate_string_manipulation()
    
    # Run tests
    run_tests()
    
    # Example usage
    print("=== Example Usage ===")
    message = "Meet me at midnight!"
    shift = 7
    
    print(f"Original message: {message}")
    encrypted = encrypt_message(message, shift)
    print(f"Encrypted (shift {shift}): {encrypted}")
    
    decrypted = decrypt_message(encrypted, shift)
    print(f"Decrypted: {decrypted}")
    
    print(f"\nBrute force decryption of '{encrypted}':")
    brute_force_decrypt(encrypted)
    
    # Uncomment the line below to run interactive mode
    # interactive_cipher()


if __name__ == "__main__":
    main()
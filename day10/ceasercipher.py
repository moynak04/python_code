def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - ascii_start + shift) % 26 + ascii_start)
            result += new_char
        else:
            result += char

    return result

# Example
message = "HELLO"
shift = 3

encrypted = caesar_cipher(message, shift)
print("Encrypted:", encrypted)
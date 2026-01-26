def encrypt(text):
    result = ""

    for char in text:
        if char.isalpha():  # check if it's a letter
            shift = 3
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # keep spaces, numbers, symbols unchanged
            result += char

    return result


# Example usage
message = input("Enter your message: ")
encrypted = encrypt(message)
print("Encrypted message:", encrypted)

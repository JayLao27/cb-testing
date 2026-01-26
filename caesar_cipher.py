from encryption import encrypt
from decryption import decrypt

print("Caesar Cipher Program")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Choose an option (1 or 2): ")
message = input("Enter your message: ")

if choice == "1":
    print("Encrypted message:", encrypt(message))
elif choice == "2":
    print("Decrypted message:", decrypt(message))
else:
    print("Invalid choice")

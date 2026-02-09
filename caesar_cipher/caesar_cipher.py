from encryption import encrypt
from decryption import decrypt

while True:
    print("\n=== Caesar Cipher Program ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choose an option (1, 2, 3): ")

    if choice == "3":
        print("Goodbye!")
        break

    message = input("Enter your message: ")
    shift = int(input("Enter shift key: "))

    if choice == "1":
        print("Encrypted message:", encrypt(message, shift))
    elif choice == "2":
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice. Please try again.")

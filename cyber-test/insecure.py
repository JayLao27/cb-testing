#Find security vulnerabilities.
#Explain the risk.
#Implement a secure solution.
def secure_input():
    
    while True:
        user_input = input("Enter your name (or 'quit' to exit): ").strip()
        
        # Validate input
        if not user_input:
            print("Please enter a valid name.")
            continue
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        print(f"Hello, {user_input}!")

if __name__ == "__main__":
    secure_input()
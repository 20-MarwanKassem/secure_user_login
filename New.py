import hashlib

user_database = {}

def register_user():
    
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user_database[username] = hashed_password

    print("Registration successful!")


def login_user():
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    hashed_password = user_database.get(username)

    if hashed_password:
        
        entered_password = hashlib.sha256(password.encode()).hexdigest()

        if entered_password == hashed_password:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")


while True:
    print("\n-- User Registration & Login System --")
    print("1. Register")
    print("2. Login")
    print("3. Exit")


    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        
        print("Exiting the program...")
        break
    else:
        
        print("Invalid choice. Please try again.")


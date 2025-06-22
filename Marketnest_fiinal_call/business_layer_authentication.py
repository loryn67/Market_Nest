from persistence_layer_authentication import user_exists, save_user, get_user_credentials, email_exists
from business_layer_dashboard import show_dashboard
import hashlib
import sys
import termios
import tty

#REGISTRATION FUNCTION
def create_account():
    print("\n--- Create Account ---")
    
    print("\n--- Market Nest Trust Policy ---")
    print("1. Users must provide accurate and truthful information.")
    print("2. Users agree to maintain the security of their account.")
    print("3. Users must not engage in fraudulent activities.")
    print("4. Users agree to respect other users and follow community guidelines.")
    print("5. Users must comply with all applicable laws and regulations.")
    
    accept = input("\nDo you agree to the trust policy? (yes/no): ").lower()
    if accept != 'yes':
        print("Account creation requires acceptance of the trust policy.")
        return

    username = input("Username: ")

    if user_exists(username):
        print("Username already exists.")
        return

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    
    if email_exists(email):
        print("This email address is already registered. Please use a different email.")
        return
        
    country = input("Country: ")
    city = input("City: ")

    password = masked_input("Enter your password: ")
    password = hashlib.sha256(password.encode()).hexdigest()

    save_user(username, first_name, last_name, email, country, city, password)
    print("Account created successfully!")
    print("Thank you for accepting our trust policy!")

#LOGIN FUNCTION
def login():
    username = input("Username: ")
    password = masked_input("Enter your password: ")

    user = get_user_credentials(username)
    if not user:
        print("Username not found.")
        return

    username_db, stored_hash, first_name = user
    if hashlib.sha256(password.encode()).hexdigest() == stored_hash:
        print("Login successful!")
        show_dashboard(username, first_name)
    else:
        print("Incorrect password.")

#PASSWORD FUNCTION
def masked_input(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch in {"\n", "\r"}:
                print()
                break
            elif ch == "\x7f":  
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
            else:
                password += ch
                print("*", end="", flush=True)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return password



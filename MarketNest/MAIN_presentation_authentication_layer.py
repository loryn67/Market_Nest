from business_layer_authentication import create_account, login
from database_layer_table_creation import initialize_database

def main_entry_point():
    initialize_database()
    while True:
        print("\n--- Welcome ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main_entry_point()
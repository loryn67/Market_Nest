from business_layer_product_management import (
    view_my_products,
    add_product,
    update_product,
    delete_product
)


def product_management_menu(username):
    while True:
        print("\n--- Product Management ---")
        print("1. View My Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            view_my_products(username)
        elif choice == "2":
            add_product(username)
        elif choice == "3":
            update_product(username)
        elif choice == "4":
            delete_product(username)
        elif choice == "5":
            break
        else:
            print("Invalid option.")
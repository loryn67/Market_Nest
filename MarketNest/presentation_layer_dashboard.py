def display_dashboard_menu(first_name):
    """Display the dashboard menu."""
    print("\n--- User Dashboard ---") 
    print(f"Hello, {first_name}! You are now logged in.")
    print("\nOptions:")
    print("1. Manage My Products")
    print("2. Search Products")
    print("3. Buy Product")
    print("4. View sold Products")
    print("5. Logout")

def get_dashboard_choice():
    """Get user choice from dashboard menu."""
    return input("Choose an option: ")

def display_product_number_input():
    """Display product number input prompt."""
    return input("\nEnter product number to buy (from the list above): ")

def display_invalid_input():
    """Display invalid input message."""
    print("Invalid option. Please choose a number between 1-5.")

def display_invalid_product_number():
    """Display invalid product number message."""
    print("Please enter a valid product number.")

def display_invalid_product_range():
    """Display invalid product range message."""
    print("Invalid product number.")

def display_logout_message():
    """Display logout message."""
    print("Logging out...")

def display_product_catalog(products):
    """Display the product catalog."""
    print("\nProduct Catalog:\n")
    
    if not products:
        print("No products found.")
        return

    for num, (pid, name, price, stock, category, created_at, first_name, last_name, image_url) in enumerate(products, 1):
        print(f"{num}. {name} | ${price:.2f} | Stock: {stock} | Category: {category}")
        print(f"Seller: {first_name} {last_name} | Added: {created_at}")
        print(f"Image URL: {image_url}")
        print("-" * 50)
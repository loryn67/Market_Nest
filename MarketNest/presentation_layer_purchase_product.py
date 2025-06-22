def show_product_details(product_details: tuple) -> None:
    """Display detailed product information to the user."""
    print("\nProduct Details:")
    print(f"ID: {product_details[0]}")
    print(f"Name: {product_details[1]}")
    print(f"Price: ${product_details[2]:.2f}")
    print(f"Category: {product_details[3]}")
    print(f"Stock: {product_details[4]}")
    print(f"Seller: {product_details[5]}")
    print(f"Description: {product_details[6]}")
    print(f"Image URL: {product_details[7]}")
    print(f"Seller Email: {product_details[8]}")

def show_purchase_confirmation(buyer_email: str, seller_email: str, product_name: str) -> None:
    print("\nPurchase Confirmed!")
    print("Email notifications have been sent to:")
    print(f"Buyer: {buyer_email}")
    print(f"Seller: {seller_email}")
    print(f"Product: {product_name}")
    print (f"The seller will contact you shortly at {buyer_email} for further details and to arrange the payment process.")
    print("\nThank you for your purchase!")

def show_purchase_error(error_message: str) -> None:
    """Show error message for purchase failure."""
    print(f"\nError: {error_message}")
    print("Purchase was not completed. Please try again.")

def confirm_the_purchase() -> None:
    """Show message when product status is pending."""
    print("\n Do you want to confirm the purchase? (yes/no): ")

def show_product_not_found() -> None:
    """Show message when product is not found."""
    print("\nProduct not found or already sold.")

def show_email_error() -> None:
    """Show message when email retrieval fails."""
    print("\nError: Could not retrieve email addresses.")
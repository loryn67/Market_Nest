from persistence_layer_purchase_product import (
    get_product_details, update_product_status, create_order, get_user_email
)
from presentation_layer_purchase_product import (
    show_product_details, show_purchase_confirmation, show_purchase_error,
    confirm_the_purchase, show_product_not_found, show_email_error
)
from persistence_layer_product_management import fetch_all_products
from presentation_layer_dashboard import display_product_catalog

def purchase_product(product_id: int, buyer_username: str) -> bool:
    try:
        # Fetch and display the product catalog
        products = fetch_all_products()
        display_product_catalog(products)

        # Validate product existence and update status to 'pending'
        product_details = get_product_details(product_id)
        if not product_details:
            show_product_not_found()
            return False
        if not update_product_status(product_id, 'pending'):
            show_purchase_error("Failed to update product status to 'pending'.")
            return False

        # Display product details and confirm purchase
        show_product_details(product_details)
        if not confirm_the_purchase():
            update_product_status(product_id, 'free')
            return False

        # Extract seller and buyer information
        seller_username = product_details[2]  # Correct index for seller username
        buyer_email = get_user_email(buyer_username)
        seller_email = product_details[4]  # Correct index for seller email

        if not buyer_email or not seller_email:
            show_email_error()
            update_product_status(product_id, 'free')
            return False

        # Create order and finalize purchase
        if create_order(product_id, buyer_username, seller_username, float(product_details[1])) and \
           update_product_status(product_id, 'sold'):
            show_purchase_confirmation(buyer_email, seller_email, product_details[0])
            return True

        # Handle purchase failure
        update_product_status(product_id, 'pending')
        show_purchase_error("Purchase failed.")
        return False

    except Exception as e:
        show_purchase_error(f"An error occurred: {str(e)}")
        update_product_status(product_id, 'free')
        return False


def confirm_the_purchase() -> bool:
    while True:
        user_input = input("\nDo you want to confirm the purchase? (yes/no): ").strip().lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            print ("Purchase cancelled.")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
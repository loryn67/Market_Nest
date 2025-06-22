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
    products = fetch_all_products()
    display_product_catalog(products)

    try:
   
        if not update_product_status(product_id, 'pending'):
            show_product_not_found()
            return False
        product_details = get_product_details(product_id)
        if not product_details:
            show_product_not_found()
            return False
        show_product_details(product_details)
        confirm_the_purchase()
        input()
        seller_username = product_details[5]
        buyer_email = get_user_email(buyer_username)
        seller_email = product_details[8]
        
        if not buyer_email or not seller_email:
            show_email_error()
            update_product_status(product_id, 'free')
            return False
        if create_order(product_id, buyer_username, seller_username, product_details[2]) and \
           update_product_status(product_id, 'sold'):
            show_purchase_confirmation(buyer_email, seller_email, product_details[1])
            return True
        update_product_status(product_id, 'pending')
        show_purchase_error("Purchase failed.")
        return False
    
    except Exception as e:
        show_purchase_error(str(e))
        update_product_status(product_id, 'free')
        return False
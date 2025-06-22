import sys
from persistence_layer_product_management import fetch_all_products
from persistence_layer_view_sold_products import fetch_sold_products_by_user
from presentation_layer_product_management import product_management_menu
from business_layer_purchase_product import purchase_product
from presentation_layer_search_cache import search_products_menu
from presentation_layer_view_sold_products import display_sold_products
from presentation_layer_dashboard import (
    display_dashboard_menu, get_dashboard_choice,
    display_product_number_input, display_invalid_input,
    display_invalid_product_number, display_invalid_product_range,
    display_logout_message, display_product_catalog
)

def show_dashboard(username, first_name):
    """Handle the complete dashboard flow."""
    while True:
        display_dashboard_menu(first_name)
        display_product_catalog(fetch_all_products())
        
        choice = get_dashboard_choice()
        
        if choice == "1":
            product_management_menu(username)
        elif choice == "2":
            search_products_menu()
        elif choice == "3":
            product_num = display_product_number_input()
            if not product_num.isdigit():
                display_invalid_product_number()
                continue
                
            products = fetch_all_products()
            if int(product_num) > len(products) or int(product_num) < 1:
                display_invalid_product_range()
                continue
                
            product_id = products[int(product_num) - 1][0] 
            if purchase_product(product_id, username):
                input("\nPress Enter to return to dashboard...")
        elif choice == "4":
            sold_products = fetch_sold_products_by_user(username)
            display_sold_products(sold_products)
        elif choice == "5":
            display_logout_message()
            sys.exit()
        else:
            display_invalid_input()
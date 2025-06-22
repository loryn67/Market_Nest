
from persistence_layer_view_sold_products import fetch_sold_products_by_user
from presentation_layer_view_sold_products import display_sold_products

def view_sold_products(username):
    sold_products = fetch_sold_products_by_user(username)
    display_sold_products(sold_products)

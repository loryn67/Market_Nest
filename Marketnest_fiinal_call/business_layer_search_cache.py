from persistence_layer_product_management import get_categories, fetch_all_products
from functools import lru_cache


@lru_cache(maxsize=5)
def search(search_term, category_filter=None):
    products = fetch_all_products()
    
    results = [
        (product_id, name, price, stock, category, created_at, seller_first, seller_last, image_url)
        for product_id, name, price, stock, category, created_at, seller_first, seller_last, image_url in products
        if (not category_filter or category == category_filter) and (search_term in name.lower() or search_term in category.lower())
    ]
    
    return results

def get_categories():
    categories = [
    "jackets",
    "bottoms",
    "dresses",
    "shoes",
    "bags",
    "accessories",
    "tops"
]
    return categories



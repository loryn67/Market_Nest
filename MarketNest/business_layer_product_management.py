
from persistence_layer_product_management import (
    insert_product,
    fetch_product_by_id_and_user,
    update_product_by_id,
    delete_product_by_id,
    fetch_all_products_by_user,
    fetch_all_products,
    get_categories
)


    
#VIEW MY PRODUCTS
def view_my_products(username):
    products = fetch_all_products_by_user(username)
    if not products:
        print("-" * 50)
        print("No products found.")
    else:
        print("\nYour Products:")
        for pid, name, description, price, stock, category, status, image_url, created_at in products:
            print(f"ID: {pid} | {name} | ${price:.2f} | Stock: {stock} | Category: {category} | Status: {status}")
            print(f"Description: {description}")
            print(f"Image URL: {image_url}")
            print(f"Created: {created_at}")
            print("-" * 50)
            
            
#ADD A PRODUCT
def add_product(username):
    name = input("Product Name: ")
    desc = input("Description: ")

    print("Available categories:")
    for category in get_categories():
        print(category)

    category_input = input("Category: ").strip().lower()
    if category_input not in get_categories():
        print("Invalid category selected.")
        return

    try:
        price = float(input("Price: "))
        stock = int(input("Stock quantity: "))
        image_url = input("Paste the image URL of the product: ")  
        insert_product(name, desc, price, category_input, stock, username, image_url)
        print("Product added.")
    except ValueError:
        print("Invalid price or stock value.")


#UPDATE A PRDOUCT 
def update_product(username):
    try:

        print("\nYour Products:")
        products = fetch_all_products_by_user(username)
        if not products:
            print("No products found.")
            return
        
        for pid, name, description, price, category, stock, status, image_url, created_at in products:
            print(f"ID: {pid} | {name} | ${price:.2f} | Stock: {stock} | Category: {category} | Status: {status}")
            print(f"Description: {description}")
            print(f"Image URL: {image_url}")
            print("-" * 50)


        pid = int(input("\nEnter Product ID to update: "))
        if not fetch_product_by_id_and_user(pid, username):
            print("Product not found or not yours.")
            return

 
        product = fetch_product_by_id_and_user(pid, username)
        if not product:
            print("Failed to fetch product details.")
            return


        print("\nCurrent Product Details:")
        print(f"Name: {product[1]}")
        print(f"Description: {product[2]}")
        print(f"Price: ${product[3]:.2f}")
        print(f"Category: {product[4]}")
        print(f"Stock: {product[5]}")
        print(f"Status: {product[6]}")
        print(f"Image URL: {product[7]}")


        name = input("\nEnter new name (leave blank to keep current): ").strip() or product[1]
        desc = input("Enter new description (leave blank to keep current): ").strip() or product[2]
        
        try:
            new_price = float(input("Enter new price (leave blank to keep current): ").strip() or str(product[3]))
            new_stock = int(input("Enter new stock quantity (leave blank to keep current): ").strip() or str(product[5]))
        except ValueError:
            print("Invalid price or stock value.")
            return

        categories = ["jackets", "bottoms", "dresses", "shoes", "bags", "accessories", "tops"]
        print("\nAvailable categories:")
        for cat in categories:
            print(f"- {cat}")

        new_category = input("Enter new category (leave blank to keep current): ").strip().lower() or product[4]
        if new_category not in categories:
            print("Invalid category.")
            return

        image_url = input("Enter new image URL (leave blank to keep current): ").strip() or product[7]


        update_product_by_id(pid, name, desc, new_price, new_category, new_stock, image_url)
        print("Product updated successfully!")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def delete_product(username):
    try:
        pid = int(input("Enter Product ID to delete: "))
        if not fetch_product_by_id_and_user(pid, username):
            print("Product not found or not yours.")
            return
        confirm = input("Are you sure you want to delete this product? (yes/no): ").lower()
        if confirm == 'yes':
            delete_product_by_id(pid)
            print("Product deleted.")
        else:
            print("Cancelled.")
    except ValueError:
        print("Invalid ID.")






def display_sold_products(sold_products):
    
    if not sold_products:
        print("\nYou haven't sold any products yet.")
    else:
        print("\n Sold Products:")
        for name, category, price, buyer_first, buyer_last, buyer_email, sold_at in sold_products:
            print(f"\nProduct: {name}")
            print(f"Category: {category}")
            print(f"Price: ${price:.2f}")
            print(f"Buyer: {buyer_first} {buyer_last}")
            print(f"Buyer Email: {buyer_email}")
            print(f"Date Sold: {sold_at}")
    
    input("\n Press Enter to return to the dashboard...")
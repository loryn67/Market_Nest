from business_layer_search_cache import search, get_categories


def search_products_menu():
    print("\nSearch Engine")
    
    while True:
        print("\nSearch Options:")
        print("1. Search by keyword")
        print("2. Search by category")
        print("3. Back to menu")
        choice = input("\nChoose option (1-3): ").strip()
        
        if choice == "3":
            return
            
        try:
            if choice == "1":
                search_term = input("\nEnter search term: ").strip().lower()
                if not search_term:
                    continue
                    
                results = search(search_term)

                if results:
                    print("\nFound products:")
                    for p in results:
                        print(f"- ID: {p[0]} | Name: {p[1]} | Price: ${p[2]:.2f} | Stock: {p[3]} | Category: {p[4]}")
                        print(f"Seller: {p[6]} {p[7]} | Added: {p[5]}")
                        print(f"Image URL: {p[8]}")
                        print("-" * 50)
                else:
                    print("No matching products found.")

            elif choice == "2":
                print("\nAvailable Categories:")
                categories = get_categories()
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                
                category_choice = input("\nEnter category number (or 0 to go back): ").strip()
                if category_choice == "0":
                    continue
                    
                try:
                    category_num = int(category_choice)
                    if 1 <= category_num <= len(categories):
                        category = categories[category_num - 1]
                        
                        search_term = input("\nEnter search term (or leave empty to display all products in this category): ").strip().lower()
                        
                        results = search(search_term=search_term, category_filter=category)

                        if results:
                            print("\nFound products:")
                            for p in results:
                                print(f"- ID: {p[0]} | Name: {p[1]} | Price: ${p[2]:.2f} | Stock: {p[3]} | Category: {p[4]}")
                                print(f"Seller: {p[6]} {p[7]} | Added: {p[5]}")
                                print(f"Image URL: {p[8]}")
                                print("-" * 50)
                        else:
                            print("No matching products found.")
                    else:
                        print("Invalid category number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
            
            print("\nCache Info:", search.cache_info())
            
        except Exception as e:
            print(f"Error: {str(e)}")

def display_results(results):
    if not results:
        print("No matching products found.")
        return
    print("\nFound products:")
    for p in results:
        print(f"ID: {p[0]} | Name: {p[1]} | Price: ${p[2]:.2f} | Stock: {p[3]} | Category: {p[4]}")
        print(f"Seller: {p[6]} {p[7]} | Added: {p[5]}")
        print(f"Image URL: {p[8]}")
        print("-" * 50)

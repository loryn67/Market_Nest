import sqlite3
from typing import Optional

conn = sqlite3.connect("marketplace.db")
cursor = conn.cursor()

def fetch_sold_products_by_user(seller_username):
    cursor.execute("""
        SELECT 
            p.name, p.category, p.price,
            u.first_name, u.last_name, u.email,
            o.ordered_at
        FROM orders o
        JOIN products p ON o.product_id = p.id
        JOIN users u ON o.buyer_username = u.username
        WHERE p.username = ?
        ORDER BY o.ordered_at DESC
    """, (seller_username,))
    return cursor.fetchall()
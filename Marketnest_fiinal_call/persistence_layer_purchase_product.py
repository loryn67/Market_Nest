import sqlite3
from typing import Optional

conn = sqlite3.connect("marketplace.db")
cursor = conn.cursor()

def create_order(product_id, buyer_username, seller_username, price):
    try:
        cursor.execute("""
            INSERT INTO orders (product_id, buyer_username, seller_username, price)
            VALUES (?, ?, ?, ?)
        """, (product_id, buyer_username, seller_username, price))
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    
def get_user_email(username):
    cursor.execute("SELECT email FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    return result[0] if result else None

def get_product_details(product_id):
    cursor.execute("""
        SELECT p.name, p.price, p.username,u.username, u.email
        FROM products p
        JOIN users u ON p.username = u.username
        WHERE p.id = ?
    """, (product_id,))
    return cursor.fetchone()


def update_product_status(product_id, status):
    cursor.execute("UPDATE products SET status = ? WHERE id = ?", (status, product_id))
    conn.commit()
    return cursor.rowcount > 0

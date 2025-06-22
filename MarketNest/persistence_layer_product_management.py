import sqlite3
from typing import Optional

conn = sqlite3.connect("marketplace.db")
cursor = conn.cursor()

def insert_product(name, description, price, category, stock, username, image_url):
    cursor.execute("""
        INSERT INTO products (name, description, price, category, stock, username, image_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, description, price, category, stock, username, image_url))
    conn.commit()

def fetch_product_by_id_and_user(pid, username):
    cursor.execute("SELECT * FROM products WHERE id = ? AND username = ?", (pid, username))
    return cursor.fetchone()

def update_product_by_id(pid, name, description, price, category, stock, image_url):
    cursor.execute("""
        UPDATE products
        SET name = ?, description = ?, price = ?, category = ?, stock = ?, image_url = ?
        WHERE id = ?
    """, (name, description, price, category, stock, image_url, pid))
    conn.commit()

def delete_product_by_id(pid):
    cursor.execute("DELETE FROM products WHERE id = ?", (pid,))
    conn.commit()

def fetch_all_products_by_user(username):
    cursor.execute("""
        SELECT id, name, description, price, stock, category, status, image_url, created_at 
        FROM products 
        WHERE username = ? AND status = 'free'
    """, (username,))
    return cursor.fetchall()

def fetch_all_products():
    cursor.execute("""
    SELECT p.id, p.name, p.price, p.stock, p.category, p.created_at, u.first_name, u.last_name, p.image_url
    FROM products p
    JOIN users u ON p.username = u.username
    WHERE p.status = 'free'
    ORDER BY p.created_at DESC
""")
    return cursor.fetchall()


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

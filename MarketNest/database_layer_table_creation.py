
import sqlite3
from typing import Optional
import os 

def initialize_database():
    conn = sqlite3.connect("marketplace.db")
    cursor = conn.cursor()

# Create the users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE,
        country TEXT,
        city TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category TEXT NOT NULL,
        stock INTEGER NOT NULL,
        status TEXT DEFAULT 'free',
        username TEXT NOT NULL,
        image_url TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (username) REFERENCES users(username)
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        buyer_username TEXT NOT NULL,
        seller_username TEXT NOT NULL,
        price REAL NOT NULL,
        ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(id),
        FOREIGN KEY (buyer_username) REFERENCES users(username),
        FOREIGN KEY (seller_username) REFERENCES users(username)
    )
    """)
    
    conn.commit()
    conn.close()
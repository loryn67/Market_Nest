
import sqlite3
from typing import Optional

conn = sqlite3.connect("marketplace.db")
cursor = conn.cursor()


#REGISTRATION AND LOGIN 
def user_exists(username):
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    return cursor.fetchone() is not None

def email_exists(email):
    """Check if an email address already exists in the database."""
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
    return cursor.fetchone() is not None


def save_user(username, first_name, last_name, email, country, city, password):
    cursor.execute("""
        INSERT INTO users (username, first_name, last_name, email, country, city, password)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (username, first_name, last_name, email, country, city, password))
    conn.commit()

def get_user_credentials(username):
    cursor.execute("SELECT username, password, first_name FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

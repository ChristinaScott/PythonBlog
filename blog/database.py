# database.py
# Handles connecting to the SQLite database and creating tables.
# This file ensures the database is ready for use.

import sqlite3

def connect_db():
    """Connect to the SQLite database."""
    conn1 = sqlite3.connect('blog.db')
    return conn1

def create_tables(conn1):
    """Create the posts table if it doesn't exist."""
    cursor = conn1.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')
    conn1.commit()
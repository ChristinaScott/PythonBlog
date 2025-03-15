# database.py
# Handles connecting to the SQLite database and creating tables.
# This file ensures the database is ready for use.

from datetime import datetime

class Post:
    def __init__(self, title, content, created_at=None):
        self.title = title
        self.content = content
        self.created_at = created_at or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        
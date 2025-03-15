# create_post.py
# Handles the logic for creating a new blog post.

from blog.database import connect_db
from blog.models import Post

def create_post():
    """Create a new blog post."""
    conn = connect_db()
    cursor = conn.cursor()

    title = input("Enter the post title: ")
    content = input("Enter the post content: ")
    post = Post(title, content)

    cursor.execute('''
    INSERT INTO posts (title, content, created_at)
    VALUES (?, ?, ?)
    ''', (post.title, post.content, post.created_at))
    conn.commit()
    conn.close()
    print("Post created successfully!")
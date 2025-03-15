# operations.py
# Contains functions for creating, viewing, and deleting blog posts.
# This file handles the main logic for interacting with the database.

from .database import connect_db
from .models import Post

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

def view_posts():
    """View all blog posts."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()

    if not posts:
        print("No posts found.")
        return

    for post in posts:
        print(f"\nID: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Content: {post[2]}")
        print(f"Created At: {post[3]}")

    conn.close()

def delete_post():
    """Delete a blog post by ID."""
    conn = connect_db()
    cursor = conn.cursor()

    post_id = input("Enter the ID of the post to delete: ")

    cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    print("Post deleted successfully!")
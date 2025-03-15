# view_posts.py
# Handles the logic for viewing all blog posts.

from blog.database import connect_db

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
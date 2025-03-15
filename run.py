# run.py
# The main script to run the blog application.
# This file handles the menu and calls functions from other modules.

from blog.database import connect_db, create_tables
from blog.operations import create_post, view_posts, delete_post

def main():
    """Main function to run the blog application."""
    # Initialize the database
    conn = connect_db()
    create_tables(conn)
    conn.close()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Create a new post")
        print("2. View all posts")
        print("3. Delete a post")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_post()
        elif choice == '2':
            view_posts()
        elif choice == '3':
            delete_post()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
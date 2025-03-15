# Python CLI Blog

A simple command-line blog application built with Python and SQLite. This project allows users to create, view, and delete blog posts directly from the terminal.

---

## Features

- **Create Posts**: Add new blog posts with a title and content.
- **View Posts**: Display all blog posts with their ID, title, content, and creation timestamp.
- **Delete Posts**: Remove a blog post by its ID.
- **Persistent Storage**: Blog posts are stored in a SQLite database (`blog.db`).

---

## Prerequisites

- Python 3.7 or higher.
- No additional installations required (SQLite is built into Python).

---
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ChristinaScott/PythonBlog.git
   cd PythonBlog
   ```

2. **Set up Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```
3. **Run the Application**
    ```bash 
    python3 run.py
    ```
---
 ## Usage
1. **Main Menu:**
When you run the program, you'll see the following menu:
```
--- Blog Menu ---
1. Create a new post
2. View all posts
3. Delete a post
4. Exit
```
2. **Create a Post:**

- Choose option `1` and follow the prompts to enter a title and content.

3. **View Posts:**

- Choose option `2` to see a list of all posts.

4. **Delete a Post:**

- Choose option `3` and enter the ID of the post you want to delete.

5. **Exit:**

- Choose option `4` to exit the program.

---
## Final Project Structure
```
PythonBlog/
├── blog/
│   ├── __init__.py
│   ├── database.py                  # Handles database connection and setup
│   ├── models.py                    # Defines the Post model
│   └── operations
|           ├── __init__.py
│           ├── create_post.py       # Handles the logic for creating a new blog post.
│           ├── delete_post.py       # Handles the logic for deleting a blog post by ID.
│           └── view_posts.py        # Handles the logic for viewing all blog posts.
├── blog.db                          # SQLite database file (created automatically)
├── run.py                           #  The main script to run the blog application
└── README.py                        # This file
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
-Built with Python's `sqlite3` module.
-Inspired by simple CLI applications for learning purposes.
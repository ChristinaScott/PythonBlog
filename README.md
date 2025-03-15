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






```
python_blog/
├── blog/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── operations.py
├── blog.db
└── run.py
```
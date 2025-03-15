# __init__.py
# This file makes the 'blog' folder a Python package.
# It can also be used to expose functions/classes for easier imports.

from .database import connect_db, create_tables
from .models import Post
from .operations import create_post, view_posts, delete_post
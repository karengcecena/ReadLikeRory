"""CRUD operations."""

from model import db, User, Book, ReadList, ToBeReadList, connect_to_db


def create_user(username, password):
    """Creates a user"""
    
    return User(username=username, password=password)

def get_user_by_username(username):
    """Gets user by their username"""

    return User.query.filter(User.username == username).first()

def create_book(title, author, poster_path):
    """Create and return a new book."""

    return Book(title=title, author=author, poster_path=poster_path)

def get_all_books():
    """Returns all books"""

    return Book.query.all()
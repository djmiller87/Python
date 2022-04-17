from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def save_book(cls, data):
        query = 'INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());'
        results = connectToMySQL('books_schema').query_db(query, data)
        return results

    @classmethod
    def get_one_book_and_favorite_authors(cls, data):
        query = 'SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;'
        results = connectToMySQL('books_schema').query_db(query, data)
        one_book = cls(results[0])
        for row in results:
            author_data = {
                'id' : row['authors.id'],
                'name' : row['name'],
                'created_at' : row['authors.created_at'],
                'updated_at': row['authors.updated_at']
            }
            one_book.authors.append(author.Author(author_data))
        return one_book

    @classmethod
    def get_all_books(cls):
        query = 'Select * FROM books;'
        results = connectToMySQL('books_schema').query_db(query)
        all_books = []
        for row in results:
            all_books.append(cls(row))
        return all_books

    @classmethod
    def add_favorite_author(cls, data):
        query = 'INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);'
        results = connectToMySQL('books_schema').query_db(query, data)
        return results

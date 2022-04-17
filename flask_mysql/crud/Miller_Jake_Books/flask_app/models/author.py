from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())'
        results = connectToMySQL('books_schema').query_db(query, data)
        return results

    @classmethod
    def get_one_author_and_favorite_books(cls, data):
        query = 'SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books on favorites.book_id = books.id WHERE authors.id = %(id)s;'
        results = connectToMySQL('books_schema').query_db(query, data)
        one_author = cls(results[0])
        for row in results:
            book_data = {
                'id' : row['books.id'],
                'title' : row['title'],
                'num_of_pages' : row['num_of_pages'],
                'created_at' : row['books.created_at'],
                'updated_at' : row['books.updated_at']
            }
            one_author.books.append(book.Book(book_data))
        return one_author


    @classmethod
    def get_all_authors(cls):
        query = 'SELECT * FROM authors;'
        results = connectToMySQL('books_schema').query_db(query) 
        authors = []  
        for row in results:
            authors.append(cls(row))     
        return authors

    @classmethod
    def add_favorite_book(cls, data):
        query = 'INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);'
        results = connectToMySQL('books_schema').query_db(query, data)
        return results






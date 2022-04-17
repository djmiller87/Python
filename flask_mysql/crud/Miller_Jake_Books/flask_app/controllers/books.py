from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def books():
    return render_template('books.html', all_books = Book.get_all_books())

@app.route('/save/book', methods = ['POST'])
def save_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
    }
    Book.save_book(data)
    return redirect('/books')

@app.route('/book/show/<int:id>')
def book_show(id):
    data = {
        'id' : id
    }
    return render_template('book_show.html', one_book = Book.get_one_book_and_favorite_authors(data), all_authors = Author.get_all_authors())

@app.route('/book/favorites', methods = ['POST'])
def add_favorite_author():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Book.add_favorite_author(data)
    return redirect(f"/book/show/{request.form['book_id']}")

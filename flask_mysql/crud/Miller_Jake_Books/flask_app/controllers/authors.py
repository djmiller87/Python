from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return render_template('index.html', all_authors = Author.get_all_authors())

@app.route('/author/show/<int:id>')
def author_show(id):
    data = {
        'id' : id
    }
    return render_template('author_show.html', one_author = Author.get_one_author_and_favorite_books(data), all_books = Book.get_all_books())

@app.route('/save/author', methods = ['POST'])
def save_author():
    data = {
        'name' : request.form['name']
    }
    Author.save(data)
    return redirect('/')

@app.route('/author/favorite', methods = ['POST'])
def add_book_to_favorites():
    favorite_data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Author.add_favorite_book(favorite_data)
    return redirect(f"/author/show/{request.form['author_id']}")
    
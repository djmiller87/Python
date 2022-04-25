from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user

@app.route('/')
def index():
    all_users = user.User.get_all()
    all_friendships = user.User.all_friendships()
    return render_template('index.html', all_users = all_users, all_friendships = all_friendships)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name']
    }
    user.User.save(data)
    return redirect('/')

@app.route('/create_friendship', methods=['POST'])
def create_friendship():
    data = {
        'user_id' : request.form['user_id'],
        'friend_id' : request.form['friend_id']
    }
    user.User.create_friendship(data)
    return redirect('/')
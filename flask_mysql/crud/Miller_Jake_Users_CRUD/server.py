from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', all_users = users)

@app.route('/new_user')
def new_user():
    return render_template('create_user.html')

@app.route('/create_user', methods = ['POST'])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    user_id = User.save(data)
    return redirect(f'/show_user/{user_id}')

@app.route('/show_user/<int:id>')
def show_user(id):
    data = {
        'id': id
    }
    one_user = User.show_a_user(data)
    return render_template('show_user.html', user_info = one_user)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        'id': id
    }
    one_user = User.show_a_user(data)
    return render_template('edit_user.html', user_info = one_user)

@app.route('/update_user/<int:id>', methods=['POST'])
def update_the_user(id):
    data = {
        'id': id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect(f'/show_user/{id}')

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
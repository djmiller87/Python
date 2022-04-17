from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html', all_emails = Email.get_all())

@app.route('/save', methods = ['POST'])
def save_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {
        'email' : request.form['email']
    }
    Email.save(data)
    return redirect('/success')

@app.route('/delete/<int:id>')
def delete_email(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect('/success')

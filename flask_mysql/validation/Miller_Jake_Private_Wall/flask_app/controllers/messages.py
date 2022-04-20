from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import message, user


@app.route('/post_message', methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')
    if not message.Message.validate_message(request.form):
        return redirect(f"/dashboard/{session['user_id']}")
    data = {
        'sender_id' : request.form['sender_id'],
        'recipient_id' : request.form['recipient_id'],
        'message' : request.form['message']
    }
    message.Message.save(data)
    return redirect(f"/dashboard/{session['user_id']}")

@app.route('/delete_message/<int:id>')
def delete_message(id):
    data = {
        'id' : id
    }
    message.Message.delete(data)
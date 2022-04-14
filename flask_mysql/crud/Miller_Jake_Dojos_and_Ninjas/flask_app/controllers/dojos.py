from flask_app import app
from flask import render_template, redirect, request, session, Flask
from flask_app.models import dojo, ninja


@app.route('/')
def index():
    return render_template('index.html', all_dojos = dojo.Dojo.get_all())

@app.route('/create_dojo', methods = ['POST'])
def create_new_dojo():
    data = {
        'name' : request.form['name']
    }
    dojo.Dojo.save(data)
    return redirect('/')

@app.route('/show_dojo/<int:id>')
def dojo_info(id):
    data = {
        'id': id
    }    
    return render_template('show_dojo.html', info_dojo = dojo.Dojo.get_one_dojo_and_ninjas(data))


from flask_app import app
from flask import render_template, redirect, request, session, Flask
from flask_app.models import dojo, ninja


@app.route('/new_ninja')
def new_ninja():
    return render_template('new_ninja.html', all_dojos = dojo.Dojo.get_all())

@app.route('/create_ninja', methods = ['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    id = request.form['dojo_id']
    ninja.Ninja.save(data)
    return redirect(f'/show_dojo/{id}')
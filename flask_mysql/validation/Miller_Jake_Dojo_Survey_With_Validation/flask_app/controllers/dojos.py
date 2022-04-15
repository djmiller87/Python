from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods = ['POST'])
def save():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
    'name': request.form['name'],
    'location': request.form['location'],
    'language':request.form['language'],
    'gender': request.form['gender'],
    'comment': request.form['comment'],
    }
    Dojo.save_survey(data)
    return redirect("/result")


@app.route('/result')
def result():
    last_info = Dojo.get_info()
    print(last_info)
    return render_template('result.html', info = last_info)

@app.route('/reset')
def reset():
    return redirect('/')
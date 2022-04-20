from email import message
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe



@app.route('/show/<int:id>')
def show(id):
    data = {
        'id' : id
    }
    data_id = {
        'id' : session['user_id']
    }
    recipe_info = recipe.Recipe.get_one_info(data)
    one_user = user.User.one_user_info(data_id)
    return render_template('recipe.html', recipe_info = recipe_info, one_user = one_user)

# _________________________________________________________________
# NEW RECIPE
# -----------------------------------------------------------------

@app.route('/new_recipe')
def new():
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    one_user = user.User.one_user_info(data)
    return render_template('new_recipe.html', one_user = one_user)

# _________________________________________________________________
# CREATE RECIPE
# -----------------------------------------------------------------

@app.route('/create', methods=['POST'])
def create():
    if 'user_id' not in session:
        return redirect('/')
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/new_recipe')
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'time' : request.form['time'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made'],
        'user_id' : session['user_id']
    }
    recipe.Recipe.save(data)
    return redirect(f"/dashboard/{session['user_id']}")

# _________________________________________________________________
# EDIT RECIPE
# -----------------------------------------------------------------

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    recipe_info = recipe.Recipe.get_one_info(data)
    return render_template('edit_recipe.html', recipe_info = recipe_info)

# _________________________________________________________________
# UPDATE RECIPE
# -----------------------------------------------------------------

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'user_id' not in session:
        return redirect('/')
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f"/edit/{id}")
    data = {
        'id' : id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'time' : request.form['time'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['date_made']

    }
    recipe.Recipe.update(data)
    return redirect(f"/dashboard/{session['user_id']}")



# _________________________________________________________________
# DELETE RECIPE
# -----------------------------------------------------------------

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    recipe.Recipe.delete(data)
    return redirect(f"/dashboard/{session['user_id']}")
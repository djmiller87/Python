from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'a_secret_key'

@app.route('/')
def index():
    if 'count' and 'number' not in  session:
        session['count'] = 0
        session['number'] = 1
    else:
        session['count'] += 1
        session['number'] += 1
    return render_template('index.html')

@app.route('/add_two')
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.pop('count')
    session.pop('number')
    session.pop('increment')
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    session['increment'] = request.form['increment']
    session['count'] += int(session['increment']) - 1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)
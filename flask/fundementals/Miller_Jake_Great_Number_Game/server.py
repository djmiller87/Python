from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'this is the key'

@app.route('/')
def index():
    if 'number' and 'attempts' not in session:
        session['number'] = random.randint(1,100)
        session['attempts'] = 0
    if session['attempts'] > 4:
        return render_template('fail.html')
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    print('we made it to here')
    print(session['number'])
    session['attempts'] += 1
    session['guess'] = request.form['guess'] or 0 
    if int(session['guess']) < int(session['number']):
        session['message'] = "Guess is too low. Try again."
    elif int(session['guess']) > int(session['number']):
        session['message'] = "Guess is too high. Try again."
    else:
        return render_template('correct.html')
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('number')
    session.pop('message')
    session.pop('guess')
    session.pop('attempts')
    return redirect('/')

@app.route('/leaderboard')
def leader_board():
    return render_template('leaderboard.html')

@app.route('/leaders', methods=['POST'])
def leaders():
    session['leadername'] = request.form['leadername']
    return render_template('leaders.html')


if __name__ == '__main__':
    app.run(debug=True)

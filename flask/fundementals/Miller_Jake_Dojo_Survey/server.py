from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'dojo servey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['gender'] = request.form['gender']
    session['comment'] = request.form['comment']
    if request.method == 'POST':
        session['system'] = request.form.getlist('system')
        line = []
        for os in session['system']:
            line.append(os)
    return render_template('result.html', opsy = line[0])

@app.route('/reset')
def reset():
    session.pop('name')
    session.pop('location')
    session.pop('language')
    session.pop('gender')
    session.pop('system')
    session.pop('comment')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

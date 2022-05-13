from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<string:name>')
def say(name):
    return "Hi " + name


@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return int(num) * (" " + word)

@app.route('/<other>')
def other(other):
    other = "Sorry! No response. Try again."
    return other

if __name__=="__main__":
    app.run(debug=True)


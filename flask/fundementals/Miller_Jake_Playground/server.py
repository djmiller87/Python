from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', times = 3, color = "lightblue")

@app.route('/play/<int:num>')
def times(num):
    return render_template('index.html', times = num, color = "lightblue")

@app.route('/play/<int:num>/<string:shade>')
def color(num, shade):
    return render_template('index.html', times = num, color = shade)

if __name__ == "__main__":
    app.run(debug = True)
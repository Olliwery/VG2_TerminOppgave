from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('home.html')


@app.route('/loginregister')
def red():
    return render_template ('loginregister.html')


@app.route('/omoss')
def blue():
    return render_template ('omoss.html')


@app.route('/kontaktoss')
def green():
    return render_template ('kontaktoss.html')


@app.route('/data')
def data():
    num = random.random()
    print(num)

    liste = "Erik, Nai, Oronai"
    return render_template ('medData.html', sendesInn = num, noeAnnet = "Her er det", Baka = liste)


if __name__ == '__main__':
    app.run(debug=True)
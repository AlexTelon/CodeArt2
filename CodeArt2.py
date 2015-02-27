from flask import Flask, render_template, g, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)

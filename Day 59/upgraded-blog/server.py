#Day 59 of Udemy's 100 Days of Python programming course
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
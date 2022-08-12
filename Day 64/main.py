from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), unique = True, nullable = False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(200), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    ranking = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String(50), nullable = False)
    img_url = db.Column(db.String(100), nullable = False)

class RateMovieForm(FlaskForm):
    rating = StringField('Your rating (Out of 10)', validators = [DataRequired()])
    review = StringField('Your review', validators = [DataRequired()])
    submit = SubmitField("Done")

db.create_all()


@app.route("/")
def home():
    return render_template("index.html", movies = db.session.query(Movie).all())

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie = movie, form = form)

if __name__ == '__main__':
    app.run(debug=True)

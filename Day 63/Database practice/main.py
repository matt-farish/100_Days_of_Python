from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ======== CREATE NEW DATABASE ======== #
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ======== CREATE NEW TABLE ======== #
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique = True, nullable = False)
    author = db.Column(db.String(250), unique = True, nullable = False)
    rating = db.Column(db.Float(), nullable = False)
    
db.create_all()

all_books = db.session.query(Book).all()

for book in all_books:
    print(book.title)
    print(book.author)
    print(book.rating)
#Day 61 of Udemy's 100 Days of Python programming course
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

error_msg = "Must be between 8 and 30 characters!"

class Form(FlaskForm):
    email = StringField(label = "Email", validators=[DataRequired(), Email()])
    password = PasswordField(label = "Password", validators=[DataRequired(), Length(8, 30)])
    submit = SubmitField(label = "Submit")


app = Flask(__name__)
app.secret_key = "SomethingSuperSecret"
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods = ["GET", "POST"])
def login():
    LoginForm = Form()
    if LoginForm.validate_on_submit():
        if LoginForm.email.data == "admin@email.com" and LoginForm.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template('login.html', form = LoginForm)

if __name__ == '__main__':
    app.run(debug=True)
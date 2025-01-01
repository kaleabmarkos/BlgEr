from flask import Flask, flash
from flask import render_template, url_for, redirect
import secrets
from flask_sqlalchemy import SQLAlchemy
from forms import Registeration, LoginForm
from datetime import datetime
app=Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.png')
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post', backref='author', lazy=True)
 
    def __repr__(self):
        return f"User('{self.user_name}','{self.email}','{self.image_file}')"
        
    
class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

    


post=[
    {
        'author':"Bill hills",
        'title':'Blogger1',
        'content':"Movie",
        'date': "Nov 1, 2022"
    }, 
    {
        'author':"John Deer",
        'title':'Blogger2',
        'content':"Music",
        'date': "Nov 3, 2022"
    },
    { 
        'author':"Bill hills",
        'title':'Blogger3',
        'content':"Movie",
        'date': "Nov 5, 2022"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=post)


@app.route("/about")
def about(): 
    return render_template("about.html", title="About our page") 

@app.route('/register',methods=["GET", "POST"])
def register():
    form = Registeration()
    if form.validate_on_submit():
        flash(f"Account created for {form.user_name.data}!", 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"{form.email.data} Logged in!", 'success')
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)

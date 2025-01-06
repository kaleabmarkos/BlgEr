from flask import flash, render_template, url_for, redirect
from blgrer.models import User, Post
from blgrer.forms import Registeration, LoginForm
from blgrer import app, db, bcrypt



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
        hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(user_name = form.user_name.data, email=form.email.data, password=hash)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.user_name.data}!", 'success')
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"{form.email.data} Logged in!", 'success')
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)


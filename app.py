import os
import random
from flask import Flask, render_template, url_for, session, request, redirect, flash
from forms import LoginForm, CreateAccountForm, CreateItem, EditAccountForm

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from models import Test_User, Test_Items, Test_Trades, Test_ItemForTrade
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(12)

basedir = os.path.abspath(os.path.dirname(__name__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir,"data.splite") #no idea what this does
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #tracks all the changes of the database

db.init_app(app)
Migrate(app, db)

#with app.app_context():
#    db.drop_all()
#    db.create_all()

@app.route("/")
def index():
    '''
    if session.get("logged_in") == True:
        return render_template("index.html")
    else:
        return redirect("login")
    '''
    

    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        pw = form.password.data
        form.username.data = ''
        form.password.data = ''
        print(f"Recorded: {name}, {pw}")

        foundUser = User.query.filter_by(username=name).first()
        #print(foundUser)
        if foundUser:
            if bcrypt.check_password_hash(foundUser.password, pw):
                session["logged_in"] = True
                session["username"] = name
                return redirect(url_for('index'))
            else:
                flash("Password is wrong")
        else:
            flash("User does not exist")

        return redirect(url_for('login'))

    return render_template("signin.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():

    form = CreateAccountForm()
    if form.validate_on_submit():
        name = form.username.data
        pw = form.password.data
        form.username.data = ''
        form.password.data = ''
        print(f"Recorded: {name}, {pw}")

        users = User.query.all()
        similarUser = User.query.filter_by(username=name).first()
        
        if similarUser:
            flash("Username already exists")
        else:
            hashed = bcrypt.generate_password_hash(password=pw)
            user = User(name, hashed)
            db.session.add(user)
            db.session.commit()
            session["logged_in"] = True
            session["username"] = name
            return redirect(url_for('index'))

    return render_template("register.html", form=form)

@app.route("/admin")
def admin():
    users = User.query.all()
    return render_template("admin.html", users=users)

@app.route("/profile")
def profile():
    if session.get("logged_in") == True:
        name = session['username']
        return redirect(f"profile/{name}") 
    flash("Please Log in")
    return redirect("login")

@app.route("/profile/<name>", methods=["GET", "POST"])
def profileName(name):
    user = User.query.filter_by(username=name).first()
    if not user:
        flash("Please Log in")
        return redirect(url_for("login"))
    print(user)

    editForm = EditAccountForm()
    if editForm.validate_on_submit():
        #create new read variables
        readDiscord = editForm.discord.data
        readDesc = editForm.description.data
        #clear form on page
        editForm.discord.data = ""
        editForm.description.data = ""
        #update database
        user.discord = readDiscord
        user.description = readDesc
        db.session.commit()
    
    #read discord and description from database
    discord = user.discord
    description = user.description
    communityUsers = user.communityUsers

    print(f"Up to date: {discord}:{description}")

    return render_template("profile.html", name=name, discord=discord, description=description, editform=editForm, communityUsers=communityUsers)

@app.route('/community')
def community():
    items = Test_Items.query.all()
    print(items)
    return render_template('community.html', items=items)

@app.route('/community/create_item', methods=["GET", "POST"])
def create_item():
    form = CreateItem()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        image = form.image.data
        item = Test_Items(name, price, image)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('community'))
    return render_template('create_item.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
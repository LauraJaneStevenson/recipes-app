from jinja2 import StrictUndefined

from flask import Flask, send_from_directory, render_template, request, flash, redirect, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Recipe, Ingredient, RecipeIngredient
# , Project, LogEntry, UserFollower, FollowingUser

from werkzeug.utils import secure_filename

import datetime

app = Flask(__name__)

# to handel uploading images
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# to use wiht flask debug tool bar
app.secret_key = "123"

@app.route("/")
def landingpage():
    """Renders homepage page"""

    return render_template("landingpage.html")

@app.route("/register")
def registeration():
    """Return registeration page"""

    return render_template("register.html")

@app.route("/add_user", methods=['POST'])
def register_user():
    """Add user to the data base"""

    # get info from form
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    # get all existing usernames
    existing_usernames = db.session.query(User.username).all()
    
    # check if username from form is already taken
    for existing_username in existing_usernames:
        
        if username == existing_username[0]:

            print("Sorry that user name is taken!")
            return redirect("/register")

    # if username not taken create new user object
    new_user = User(name=name,username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")



@app.route("/login", methods=['POST'])
def login_proccess():
    """Logs in user and redirect to user dashboard"""

    # getting login info from form
    username = request.form["username"]
    password = request.form["password"]

    # query for user
    user = User.query.filter_by(username=username,password=password).first()

    if user == None:
        flash("User does not exist, click register to start your Creative Blog!")
        return redirect("/")
    if user.password != password: 
        flash("Incorrect password.")

    # add user_id to the session 
    session["user_id"] = user.user_id
    session["name"] = user.name
    session["username"] = user.username

    return redirect("/dashboard")

@app.route("/dashboard", methods=["GET"])
def show_dashboard():
    """Show user dashboard"""
    user = User.query.filter_by(user_id=session['user_id']).one()
    recipes = Recipes.query.filter_by(user_id=session['user_id'].all())
    

    return render_template("dashboard.html",user=user,recipes=recipes)



























from flask_sqlalchemy import SQLAlchemy
import os
import datetime

# Instantiate a SQLAlchemy object.
db = SQLAlchemy()

class User(db.Model):
    """Data model for a user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String,
                     nullable=False)
    username = db.Column(db.String(30),
                         nullable=False)
    password = db.Column(db.String(30),
                         nullable=False)
    recipe = db.relationship("Recipe")

    # profile_pic = db.Column(db.String(200),
    #                         default="/static/uploads/icon.jpg")

    def __repr__(self):
        """Returns readable info about an instance of a user object."""

        return f"<Name: {self.name}, User_ID: {self.user_id}, Username: {self.username}>"

class Recipe(db.Model):
    """Data model for recipes"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer,
                           autoincrement=True, 
                           primary_key=True)
    recipe_name = db.Column(db.String,
                            nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    date = db.Column(db.DateTime,nullable=False)

    user = db.relationship("User")


    def __repr__(self):
        """Returns readable info about Project objects"""

        return f"<Recipe_Name: {self.recipe_name} Recipe_ID: {self.recipe_id} User_ID: {self.user_id}>"


# Connect db to app
def connect_to_db(app,dburi='postgres:///recipes'):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = dburi
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_ECHO"] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from flask import Flask
    app = Flask(__name__)
    #we can lean the line below out for now bc we dont have out app yet
    # from server import app
    connect_to_db(app)
    print("Connected to DB")
    db.create_all()

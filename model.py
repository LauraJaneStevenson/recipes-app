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
    description = db.Column(db.Text,
                            nullable=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    date = db.Column(db.DateTime,nullable=False)

    instuctions = db.Column(db.Text,
                            nullable=True)
    recipe_ingredient = db.relationship('RecipeIngredient')

    user = db.relationship("User")


    def __repr__(self):
        """Returns readable info about Project objects"""

        return f"<Recipe_Name: {self.recipe_name} Recipe_ID: {self.recipe_id} User_ID: {self.user_id}>"

class Ingredient(db.Model):
    """Data model for ingredients"""
    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer,
                           autoincrement=True, 
                           primary_key=True)
    ingredient_name = db.Column(db.String,
                            nullable=False)
    recipe_ingredient = db.relationship('RecipeIngredient')

    def __repr__(self):
        """Returns readable info about ingredient objects"""
        return f"<Ingredient_Name: {self.ingredient_name}, Ingredient_ID: {self.ingredient_id}>"

class RecipeIngredient(db.Model):
    """Data model for an ingredient used in a recipe"""

    __tablename__ = "recipe_ingredients"

    RecipeIngredient_id = db.Column(db.Integer,
                           autoincrement=True, 
                           primary_key=True)
    ingredient_id = db.Column(db.Integer,
                        db.ForeignKey('ingredients.ingredient_id'),
                        nullable=False)
    recipe_id = db.Column(db.Integer,
                        db.ForeignKey('recipes.recipe_id'),
                        nullable=False)
    quantity = db.Column(db.String,
                     nullable=False)

    recipe = db.relationship('Recipe')

    ingredient = db.relationship('Ingredient')

    def __repr__(self):
        """Returns readable info about recipe_ingredient objects"""

        return f"<RI_ID: {self.RecipeIngredient_id} Ingredient_ID: {self.ingredient_id}, Recipe: {self.recipe_id}"

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
    # db.create_all()

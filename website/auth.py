from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/", methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form.get("username")
        print(username)

        # checks if username field is empty
        if username is "":
            print("Empty username field")
            flash("Enter a Username.", category="empty_username")
        # checking if the username already exists
        elif db.session.query(User.username).filter_by(username=username).first() is not None:
            flash("User already exists", category="taken_username")
        # adding user to database
        else:
            new_user = User(username=username)
            db.session.add(new_user)
            db.session.commit()
            print("Account created")
            return redirect(url_for("views.home"))

    return render_template("sign-in.html")


@auth.route("/game", methods=["GET", "POST"])
def game():
    return render_template("game.html")

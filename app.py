"""Blogly application."""

import os

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

db.drop_all()
db.create_all()


@app.get('/')
def homepage():

    print('homepage')
    return redirect("/users")


@app.get('/users/new')
def show_form():
    return render_template("signup.html")

#app.route('/users/new'):
    #def show/signup:
    # if method = POST:
    # render_template


@app.post('/users/new')
def signup():
    """Gets user signup form data"""
    print('signup POST /users/new')

    first_name = request.form.get("first-name")

    last_name = request.form.get("last-name")
    last_name = last_name if last_name else None

    img_url = request.form.get("img-url")
    img_url = img_url if img_url else None

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.get("/users/<int:user_id>")

def show_user(user_id):
    """Shows user info"""
    user = User.query.get_or_404(user_id)
    return render_template("user-info.html", user=user)


@app.get("/users")
def show_users():
    """Shows all users"""

    # users = User.query.get_or_404.all(user_id)
    users = User.query.all()

    return render_template("user-list.html", users=users)


@app.get("/users/<int:user_id>/edit")
def show_edit_user(user_id):

    user = User.query.get_or_404(user_id)

    return render_template("edit-user.html", user=user)


@app.post("/users/<int:user_id>/edit")
def edit_user(user_id):

    user = User.query.filter_by(id = user_id)

    first_name = request.form.get("first-name")
    if first_name:
        user.first_name = first_name

    last_name = request.form.get("last-name")
    if last_name:
        user.last_name = last_name

    img_url = request.form.get("img-url")
    if img_url:
        user.img_url = img_url

    # update user info
    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.get("/users/<int:user_id>/delete")
def confirm_delete(user_id):

    user = User.query.get_or_404(user_id)

    return render_template('delete-user.html', user=user)


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):

    # add a flash msg?

    # user = User.query.filter_by(id = user_id)
    # user.query.delete()

    User.query.filter_by(id = user_id).delete()
    db.session.commit()

    return redirect('/')
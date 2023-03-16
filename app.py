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

#docstrings for homepage, show_form
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

    first_name = request.form.get("first-name")

    last_name = request.form.get("last-name")
    last_name = last_name if last_name else None

    image_url = request.form["image-url"] or None #..., None)
    image_url = image_url if image_url else None

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
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

    # users = User.query.get_or_404.all()
    users = User.query.all()

    return render_template("user-list.html", users=users)


@app.get("/users/<int:user_id>/edit")
def show_edit_user(user_id):
    """Shows edit user page"""
    user = User.query.get_or_404(user_id)

    return render_template("edit-user.html", user=user)


@app.post("/users/<int:user_id>/edit")
def edit_user(user_id):
    """gets edit form data and updates user"""
    user = User.query.get(user_id) #or_404

    new_first_name = request.form.get("first-name")
    if new_first_name:
        user.first_name = new_first_name

    new_last_name = request.form.get("last-name") #can't delete last name
    if new_last_name:
        user.last_name = new_last_name

    new_image_url = request.form.get("image-url") #can't delete without new photo
    if new_image_url:
        user.image_url = new_image_url

    # update user info
    db.session.commit()

    return redirect('/users')


@app.get("/users/<int:user_id>/delete")
def confirm_delete(user_id):

    user = User.query.get_or_404(user_id)

    return render_template('delete-user.html', user=user)


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):

    # TODO: add a flash msg?

    User.query.filter_by(id = user_id).delete()
    db.session.commit()

    return redirect('/')
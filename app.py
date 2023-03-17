from datetime import datetime

"""Blogly application."""

import os

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

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
    """ Homepage - redirects to /users """

    print('homepage')
    return redirect("/users")


@app.get('/users/new')
def show_form():
    """Shows the signup form for new users"""

    return render_template("signup.html")


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

    user.first_name = request.form.get("first-name", user.first_name)
    user.last_name = request.form.get("last-name", "")
    user.image_url = request.form.get("image-url", "")

    # update user info
    db.session.commit()

    return redirect('/users')


@app.get("/users/<int:user_id>/delete")
def confirm_delete(user_id):
    """Shows the delete confirmation page"""

    user = User.query.get_or_404(user_id)

    return render_template('confirm-delete.html', user=user)


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """Deletes user from database and redirects home"""

    # TODO: add a flash msg?

    User.query.filter_by(id = user_id).delete()
    db.session.commit()

    return redirect('/')


# BLOG POST ROUTES


@app.get('/users/<int:user_id>/posts/new')
def show_post_form(user_id):
    """Show form to add a post for that user"""

    user = User.query.get_or_404(user_id)

    return render_template('post-form.html', user=user)


@app.post('/users/<int:user_id>/posts/new')
def add_post(user_id):
    """Handle add form; add post and redirect to the user detail page"""

    # TODO: what if the field is left blank? flash msgs?
    title = request.form.get("title")
    content = request.form.get("content")
    # created_at = 'This very moment'

    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()

    return redirect(f'/users/{user_id}')
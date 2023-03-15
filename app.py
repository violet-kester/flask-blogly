"""Blogly application."""

import os

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///blogly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

db.drop_all()
db.create_all()


app.get('/')
def homepage():
    return redirect("/users")

app.get('/users/new')
def show_form():
    render_template("signup.html")

#app.route('/users/new'):
    #def show/signup:
        # if method = POST:
    # render_template


app.post('/users/new')
"""Gets user signup form data"""
def signup():

    first_name = request.form("first-name")

    last_name = request.form("last-name")
    last_name = last_name if last_name else None

    img_url = request.form("img-url")
    img_url = img_url if img_url else None

    user = User(first_name, last_name, img_url)
    db.session.add(user)
    db.session.commit()

    redirect(f"/users/{user.id}")

app.get("/users/<int:user_id>")
"""Shows user info"""
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user-info.html", user=user)

app.get("/users")
"""Shows all users"""
def show_users(users):
    users = User.query.get_or_404.all()
    render_template("user-list.html", users=users)

app.get("/users/<int:user_id>/edit")
def show_edit_user(user_id):

    return render_template("edit-user.html")

app.post("/users/<int:user_id>/edit")
def edit_user(user_id):


    first_name = request.form("first-name")
    first_name = first_name if first_name else None

    last_name = request.form("last-name")
    last_name = last_name if last_name else None

    img_url = request.form("img-url")
    img_url = img_url if img_url else None


    return render_template("/users")


app.post("/users/<int:user_id>/delete")
def delete_user(user_id):

    user = User.query.filter_by(id = user_id)
    db.session.delete(user)
    db.session.commit()
    redirect('/')
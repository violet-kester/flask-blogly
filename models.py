"""Models for Blogly."""

DEFAULT_IMAGE_URL = 'https://post.healthline.com/wp-content/uploads/2020/08/coconut-nutrition-correct-732x549-thumbnail-732x549.jpg'
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    first_name = db.Column(
        db.String(50),
        nullable=False)

    last_name = db.Column(
        db.String(50),
        nullable=True)

    image_url = db.Column(
        db.String(150),
        nullable=True)

    # unique(first_name, last_name)


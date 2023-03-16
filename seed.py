"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# An alternative if you don't want to drop
# and recreate your tables:
# Pet.query.delete()

# Add pets
huse = User(first_name='Huse', last_name='Kivrak', img_url='https://i5.walmartimages.com/asr/81131765-9311-47ed-ae77-15dddde6b01d.7363231977ed5579d57e0b24cd7c1d9f.png')
violet = User(first_name='Violet', last_name='Kester', img_url='https://images.heb.com/is/image/HEBGrocery/001945935?fit=constrain,1&wid=800&hei=800&fmt=jpg&qlt=85,0&resMode=sharp2&op_usm=1.75,0.3,2,0')

# Add new objects to session, so they'll persist
db.session.add(huse)
db.session.add(violet)

# Commit--otherwise, this never gets saved!
db.session.commit()

"""Seed file to make sample data for users db."""

from models import User, Post, db
from datetime import datetime
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
# An alternative if you don't want to drop
# and recreate your tables:
# Pet.query.delete()

# Add users
huse = User(first_name='Huse', last_name='Kivrak', image_url='https://i5.walmartimages.com/asr/81131765-9311-47ed-ae77-15dddde6b01d.7363231977ed5579d57e0b24cd7c1d9f.png')
violet = User(first_name='Violet', last_name='Kester', image_url='https://images.heb.com/is/image/HEBGrocery/001945935?fit=constrain,1&wid=800&hei=800&fmt=jpg&qlt=85,0&resMode=sharp2&op_usm=1.75,0.3,2,0')


post1 = Post(
    title='The Reality of Patrol Duty',
    content="""As a police officer in New York freakin' City, my daily work can be both thrillin' and
    challengin'. But sometimes it can also be freakin' mundane and exhaustin'. There are days when I
    feel like I'm just freakin' goin' through the motions, patrollin' the same freakin' streets over
    and over again. And then there are the freakin' darker moments, when I have to deal with violent
    crimes or confront the harsh realities of freakin' poverty and inequality. But even in these
    moments, I stay freakin' focused on the task at hand and try to make a freakin' difference in the
    lives of the people I serve.""",
    created_at=datetime.now(),
    user_id=1
)

post2 = Post(
    title='The Toll of Working Night Shifts',
    content="""Workin' night shifts as a freakin' police officer in New York City can be tough on both
    my body and my freakin' mind. The long hours and irregular sleep patterns can freakin' take a toll
    on my health and my freakin' relationships. But I know that this is a freakin' essential part of
    the job, and that by workin' nights, I'm helpin' to keep the freakin' city safe while most people
    are freakin' asleep. So even on the toughest nights, I stay freakin' positive and focused on the
    freakin' mission.""",
    created_at=datetime.now(),
    user_id=1
)

post3 = Post(
    title='The Importance of Self-Care',
    content="""Bein' a freakin' police officer is a demandin' job, and it's freakin' easy to get caught
     up in the freakin' stress and intensity of the work. That's why I freakin' prioritize self-care,
     both on and off the freakin' job. Whether it's takin' a few freakin' minutes to meditate during a
     break, goin' for a freakin' run after my freakin' shift, or spendin' quality time with my freakin'
     loved ones, these small freakin' acts of self-care help me to stay freakin' grounded and resilient
     in the freakin' face of the challenges I encounter as a freakin' police officer in New York City.""",
    created_at=datetime.now(),
    user_id=1
)

# Add new objects to session, so they'll persist
db.session.add(huse)
db.session.add(violet)
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)

# Commit--otherwise, this never gets saved!
db.session.commit()

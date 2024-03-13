from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    user1 = User(
        name='Demo-lition', email='demo@gmail.com', password='password', is_artist=False)
    user2 = User(
        name='Demo-lition2', email='demo2@gmail.com', password='password', is_artist=False)
    user3 = User(
        name='Pink Floyd', email='pinkfloyd@gmail.com', password='password', image_url="image url", is_artist=True)
    user4 = User(
        name='Ye', email='ye@yeye.com', password='yeyeye', image_url="image url", is_artist=False)
    user5 = User(
        name='John Mayer', email='john@mayer.com', password='password', image_url="image url", is_artist=True)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()

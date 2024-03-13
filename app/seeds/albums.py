from app.models import db, Album, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


# Adds a demo user, you can add other users here if you want
def seed_albums():
    album1 = Album(
        name='The Dark Side of the Moon', release_date=date(1973,3,1), album_type='album', image_url='image url', genre='rock', artist_id=3)
    album2 = Album(
        name='The Life of Pablo', release_date=date(2016,2,14), album_type='album', image_url='image url', genre='hiphop', artist_id=4)
    album3 = Album(
        name='Lift Yourself', release_date=date(2018,4,29), album_type='single', image_url='image url', genre='hiphop', artist_id=4)
    album4 = Album(
        name='Room for Squares', release_date=date(2001,8,16), album_type='album', image_url='image url', genre='pop', artist_id=5)

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()

from app.models import db, Track, environment, SCHEMA
from sqlalchemy.sql import text


def seed_tracks():
    track1 = Track(
        name='On The Run', duration=215, file='path to file', artist_id=3, album_id=1)
    track2 = Track(
        name='I Love Kanye', duration=44, file='path to file', artist_id=4, album_id=2)
    track3 = Track(
        name='Lift Yourself', duration=147, file='path to file', artist_id=4, album_id=3)
    track4 = Track(
        name='3x5', duration=289, file='path to file', artist_id=5, album_id=4)


    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tracks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tracks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM tracks"))

    db.session.commit()

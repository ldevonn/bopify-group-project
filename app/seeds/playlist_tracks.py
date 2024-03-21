from app.models import db, PlaylistsTracks, environment, SCHEMA
from sqlalchemy.sql import text


def seed_playlist_tracks():
    playlist1 = PlaylistsTracks(
        track_id=1, playlist_id=1)
    playlist2 = PlaylistsTracks(
        track_id=2, playlist_id=2)



    db.session.add(playlist1)
    db.session.add(playlist2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_playlist_tracks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))

    db.session.commit()

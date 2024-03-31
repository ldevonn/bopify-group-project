from app.models import db, PlaylistsTracks, environment, SCHEMA
from sqlalchemy.sql import text, insert


def seed_playlists_tracks():
    playliststracks = [
        {'track_id': 1, 'playlist_id': 1},
        {'track_id': 1, 'playlist_id': 2},
        {'track_id': 3, 'playlist_id': 1},
        {'track_id': 2, 'playlist_id': 2},
    ]

    db.session.execute(insert(PlaylistsTracks), playliststracks)
    db.session.commit()

def undo_playlists_tracks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlistsTracks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlistsTracks"))
    db.session.commit()

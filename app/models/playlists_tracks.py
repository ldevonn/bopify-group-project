from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey

PlaylistsTracks = db.Table('playlists_tracks',
    db.Model.metadata,
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.id'), nullable=False),
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), nullable=False)
)

if environment == "production":
    PlaylistsTracks.schema = SCHEMA
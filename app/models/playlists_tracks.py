from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey

table_name = 'playlists_tracks'
if environment == "production":
    table_name = add_prefix_for_prod(table_name)

PlaylistsTracks = db.Table(table_name,
    db.Model.metadata,
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.id'), nullable=False),
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), nullable=False)
)

if environment == "production":
    PlaylistsTracks.schema = SCHEMA

from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey

table_name = 'playlistsTracks'

PlaylistsTracks = db.Table(table_name,
    db.Model.metadata,
    db.Column('track_id', db.Integer, db.ForeignKey(add_prefix_for_prod('tracks.id')), nullable=False),
    db.Column('playlist_id', db.Integer, db.ForeignKey(add_prefix_for_prod('playlists.id')), nullable=False)
)

if environment == "production":
    PlaylistsTracks.schema = SCHEMA

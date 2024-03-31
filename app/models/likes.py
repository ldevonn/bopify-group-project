from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey

Like = db.Table('likes',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False),
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.id'), nullable=False)
)

if environment == "production":
    Like.schema = SCHEMA
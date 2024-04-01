from .db import db, environment, SCHEMA, add_prefix_for_prod

Like = db.Table('likes',
    db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False),
    db.Column('track_id', db.Integer, db.ForeignKey(add_prefix_for_prod('tracks.id')), nullable=False)
)

if environment == "production":
    Like.schema = SCHEMA
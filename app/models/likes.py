from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey

Like = db.Table('likes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False)
)

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'userId': self.user_id,
    #         'trackId': self.track_id,
    #     }
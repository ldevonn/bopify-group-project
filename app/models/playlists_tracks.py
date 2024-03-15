from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class PlaylistsTracks(db.Table):
    __tablename__ = 'playlistsTracks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    track_id = db.Column(db.Integer, ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False)
    playlist_id = db.Column(db.Integer, ForeignKey('playlists.id', ondelete='CASCADE'), nullable=False)
    

    def to_dict(self):
        return {
            'id': self.id,
            'trackId': self.track_id,
            'playlistId': self.playlist_id
        }

# class Child(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     parent_id = db.Column(db.Integer, ForeignKey('parent.id', ondelete='CASCADE'))
#     parent = relationship("Parent", back_populates="children")
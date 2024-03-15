from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class PlaylistsTracks(db.Model):
    __tablename__ = 'playlistsTracks'

    track = relationship("Track", back_populates="playlistsTracks")
    playlist = relationship("Playlist", back_populates="playlistsTracks")

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False)
    playlist_id = db.Column(db.Integer, ForeignKey('playlists.id', ondelete='CASCADE'), nullable=False)
    

    def to_dict(self):
        return {
            'id': self.id,
            'track_id': self.track_id,
            'playlist_id': self.playlist_id
        }

# class Child(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     parent_id = db.Column(db.Integer, ForeignKey('parent.id', ondelete='CASCADE'))
#     parent = relationship("Parent", back_populates="children")
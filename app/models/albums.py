from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Album(db.Model):
    __tablename__ = 'albums'

    tracks = relationship("Track", back_populates="album")
    artists = relationship("User", back_populates="albums")

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    album_type = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(40), nullable=False)
    artist_id = db.Column(db.Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'albumId': self.id,
            'name': self.name,
            'releaseDate': self.release_date,
            'albumType': self.album_type,
            'imageUrl': self.image_url,
            'genre': self.genre,
            'artistId': self.artist_id
        }

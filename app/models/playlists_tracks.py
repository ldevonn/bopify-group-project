from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey

PlaylistsTracks = db.Table('playlistsTracks',
    db.Model.metadata,
    db.Column('track_id', db.Integer, db.ForeignKey('tracks.id'), nullable=False),
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), nullable=False)
)

if environment == "production":
    PlaylistsTracks.schema = SCHEMA
    
    

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'trackId': self.track_id,
    #         'playlistId': self.playlist_id
    #     }

# class Child(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     parent_id = db.Column(db.Integer, ForeignKey('parent.id', ondelete='CASCADE'))
#     parent = relationship("Parent", back_populates="children")
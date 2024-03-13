from flask import Blueprint, request
from app.models import Album, Track, db
# from flask_login import current_user, login_required

album_routes = Blueprint('albums', __name__)

# Get all Albums
@album_routes.route('/')
def get_all_albums():
    albums = Album.query.all()
    # print(data)
    return {'albums': [album.to_dict() for album in albums]}

# Get an Album by albumId
@album_routes.route('/<int:album_id>')
def get_album_by_id(album_id):
    album = Album.query.get(album_id).to_dict()
    tracks = Track.query.filter(Track.album_id == album_id)
    album['tracks'] = [track.to_dict() for track in tracks]
    return album

# Get albums by artistId

# Get albums by current user (Artist)

# Create an album

# Edit an album

# Delete an album by albumId
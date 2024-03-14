from flask import Blueprint, request
from app.models import Album, Track, User, db
# from flask_login import current_user, login_required

album_routes = Blueprint('albums', __name__)

# Get all Albums
@album_routes.route('/')
def get_all_albums():
    albums = Album.query.all()
    print(albums)
    return {'albums': [album.to_dict() for album in albums]}

# Get an Album by albumId
@album_routes.route('/<int:album_id>')
def get_album_by_id(album_id):
    album = Album.query.get(album_id).to_dict()
    tracks = Track.query.filter(Track.album_id == album_id)
    album['tracks'] = [track.to_dict() for track in tracks]
    return album

# Get albums by artistId
@album_routes.route('artists/<int:artist_id>')
def get_album_by_artistId(artist_id):
    albums = Album.query.filter(Album.artist_id == artist_id).all()
    albums_with_tracks = []

    for album in albums:
        album_data = album.to_dict()
        tracks = Track.query.filter(Track.album_id == album.id)
        album_data['tracks'] = [track.to_dict() for track in tracks]
        albums_with_tracks.append(album_data)
    return albums_with_tracks

# Get albums by current user (Artist)
@album_routes.route('/current')
def get_album_by_current_user():
    pass

# Create an album
@album_routes.route('/')
def create_album():
    pass

# Edit an album
@album_routes.route('/<int:album_id>')
def edit_album():
    pass

# Delete an album by albumId
@album_routes.route('/<int:album_id>')
def delete_album():
    pass

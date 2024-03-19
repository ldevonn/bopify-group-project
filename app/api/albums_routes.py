from flask import Blueprint, request, jsonify, render_template, redirect
from flask_login import current_user, login_required
from app.models import Album, Track, User, db
from ..forms import CreateAlbumForm


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
    album = Album.query.get(album_id)

    if not album:
        response = jsonify({"message": "Album couldn't be found"})
        response.status_code = 404
        return response

    tracks = Track.query.filter(Track.album_id == album_id)
    album['tracks'] = [track.to_dict() for track in tracks]
    return album.to_dict()


# Get albums by artistId
@album_routes.route('artists/<int:artist_id>')
def get_album_by_artistId(artist_id):
    albums = Album.query.filter(Album.artist_id == artist_id).all()

    if not albums:
        response = jsonify({"message": "Artist couldn't be found"})
        response.status_code = 404
        return response

    albums_with_tracks = []

    for album in albums:
        album_data = album.to_dict()
        tracks = Track.query.filter(Track.album_id == album.id)
        album_data['tracks'] = [track.to_dict() for track in tracks]
        albums_with_tracks.append(album_data)
    return albums_with_tracks


# Get albums by current user (Artist)
@album_routes.route('/current')
@login_required
def get_album_by_current_user():

    albums = Album.query.filter(Album.artist_id == current_user.id).all()
    albums_with_tracks = []

    for album in albums:
        album_data = album.to_dict()
        tracks = Track.query.filter(Track.album_id == album.id)
        album_data['tracks'] = [track.to_dict() for track in tracks]
        albums_with_tracks.append(album_data)
    return albums_with_tracks

#--------------------------------------------------------continue here
# Create an album
@album_routes.route('/new', methods = ['GET', 'POST'])
@login_required
def create_album():

    user_id = current_user.id
    user = User.query.filter_by(id=user_id).one().to_dict()

    # print(current_user.id)

    if not user['isArtist']:
        response = jsonify({"message": "User is not an artist. Only artists can create Albums."})
        response.status_code = 403
        return response

    form = CreateAlbumForm()

    if user['isArtist']:
        if form.validate_on_submit():
            data = form.data
            new_album = Album(name = data["name"],
                              release_date = data["releaseDate"],
                              album_type = data["albumType"],
                              genre = data["genre"],
                              image_url = data["imageUrl"],
                              artist_id = current_user.id)
            db.session.add(new_album)
            db.session.commit()
            album = Album.query.get(new_album.id).to_dict()
            return "album created"
        return render_template('create_album.html', form=form)
        # return 'This user is an artist'

    return "create album blank form"

# Edit an album
@album_routes.route('/<int:album_id>')
def edit_album():
    pass

# Delete an album by albumId
@album_routes.route('/<int:album_id>', methods = ['DELETE'])
@login_required
def delete_album(album_id):
    album = Album.query.get(album_id)

    if not album:
        response = jsonify({"message": "Album couldn't be found"})
        response.status_code = 404
        return response

    if album.artist_id != current_user.id:
        response = jsonify({"message": "You are not authorized to delete this album"})
        response.status_code = 403
        return response

    db.session.delete(album)
    db.session.commit()
    return jsonify({"message": "Successfully Deleted"})

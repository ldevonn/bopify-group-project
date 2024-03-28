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
@album_routes.route('/<int:album_id>', methods=['GET', 'PUT', 'DELETE'])
def get_album_by_id(album_id):
    album = Album.query.get(album_id)

    if not album:
        response = jsonify({"message": "Album couldn't be found"})
        response.status_code = 404
        return response

    if request.method in ["PUT", "DELETE"] and album.artist_id != current_user.id:
        return jsonify({"message": "Unauthorized access"}), 403

    if request.method == 'GET':
        tracks = [track.to_dict() for track in album.tracks]
        return {**album.to_dict(), 'tracks': tracks}
        # tracks = Track.query.filter(Track.album_id == album_id)
        # album.tracks = [track.to_dict() for track in tracks]
        # return album.to_dict()

    if request.method == "PUT":
        form = CreateAlbumForm(obj=album)

        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            album.name = form.name.data
            album.releaseDate = form.releaseDate.data
            album.albumType = form.albumType.data
            album.genre = form.genre.data
            album.imageUrl = form.imageUrl.data

            db.session.commit()
            return jsonify({"message": "Album has been updated successfully"})
        else:
            error_messages = {}
            for field, errors in form.errors.items():
                error_messages[field] = errors[0]

            response = jsonify({
                "message": "Bad Request",
                "errors": error_messages,
            })
            response.status_code = 400
            return response

    if request.method == 'DELETE':
        db.session.delete(album)
        db.session.commit()
        return jsonify({"message": "Successfully Deleted"})


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

# Create an album
@album_routes.route('/new', methods=['GET', 'POST'])
@login_required
def create_album():

    user_id = current_user.id
    user = User.query.filter_by(id=user_id).one().to_dict()

    if not user['isArtist']:
        response = jsonify({"message": "User is not an artist. Only artists can create Albums."})
        response.status_code = 403
        return response
    else:
        form = CreateAlbumForm()

        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            name = form.name.data
            releaseDate = form.releaseDate.data
            albumType = form.albumType.data
            genre = form.genre.data
            imageUrl = form.imageUrl.data

            new_album = Album(name = name,
                            release_date = releaseDate,
                            album_type = albumType,
                            genre = genre,
                            image_url = imageUrl,
                            artist_id = current_user.id)
            db.session.add(new_album)
            db.session.commit()
            # album = Album.query.get(new_album.id).to_dict()
            return jsonify({"message": "Album successfully created."}), 201
        
        errors = {}
        for field, error in form.errors.items():
            field_obj = getattr(form, field)
            errors[field_obj.label.text] = error[0]
        error_response = {
            "message": "Body validation errors",
            "errors": errors
        }
        return jsonify(error_response), 400

        return render_template('create_album.html', form=form)

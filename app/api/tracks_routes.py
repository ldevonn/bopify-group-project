from flask import Blueprint, jsonify, abort, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Track, User, Album, db
from ..forms import TrackForm

track_routes = Blueprint('tracks', __name__)


@track_routes.route('/', methods=["GET"])
def get_all_tracks():
    """
    Query for all tracks and returns them in a list of track dictionaries
    """
    tracks = Track.query.all()
    return {'tracks': [track.to_dict() for track in tracks]}


@track_routes.route('/<int:track_id>', methods=["GET", "PUT", "DELETE"])
def get_or_update_or_delete_track(track_id):
    """
    Query for 
    getting a track by track id (GET) 
    OR editing a track by track id (PUT) 
    OR deleting a track by track id (DELETE)
    """
    track = Track.query.get(track_id)

    if not track:
        response = jsonify({"message": "Track couldn't be found"})
        response.status_code = 404
        return response
    
    if request.method == 'GET':
        return track.to_dict()
    if request.method == "PUT":
        form = TrackForm(obj=track)
        albums = Album.query.filter_by(artist_id=current_user.id).all()
        form.albumId.choices = [(album.id, album.name) for album in albums]

        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            track.name = form.name.data
            track.duration = form.duration.data
            track.file = form.file.data
            track.album_id = form.albumId.data

            db.session.commit()
            return jsonify({"message": "Track has been updated successfully"})
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
        db.session.delete(track)
        db.session.commit()
        return jsonify({"message": "Track deleted successfully"})
        

@track_routes.route('/current', methods=["GET"])
@login_required
def get_artist_tracks():
    """
    Query for getting all tracks created by a user. Only artist-type users should get a list returned
    """
    user_id = current_user.id
    tracks = Track.query.filter_by(artist_id=user_id).all()

    if not tracks:
        response = jsonify({"message": "User is not an artist and/or does not have any uploaded tracks"})
        return response
    
    return jsonify([track.to_dict() for track in tracks])


@track_routes.route('/new', methods=["GET", "POST"])
@login_required
def create_track():
    """
    Query for an artist to create a track. The user must be an artist, and the artist must be logged in.
    """
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).one().to_dict()

    if not user['isArtist']:
        response = jsonify({"message": "User is not an artist. Only artists can upload tracks."})
        response.status_code = 403
        return response
    else:
        form = TrackForm()
        albums = Album.query.filter_by(artist_id=user_id).all()
        form.albumId.choices = [(album.id, album.name) for album in albums]

        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            name = form.name.data
            duration = form.duration.data
            file = form.file.data
            albumId = form.albumId.data

            new_track = Track(
                name=name,
                duration=duration,
                file=file,
                artist_id=user_id,
                album_id=albumId,
            )
            db.session.add(new_track)
            db.session.commit()

            return Track.query.filter_by(name=form.name.data).order_by(Track.id.desc()).first().to_dict()
            # return redirect(url_for('tracks.get_all_tracks'))

        return render_template('create_track.html', form=form)
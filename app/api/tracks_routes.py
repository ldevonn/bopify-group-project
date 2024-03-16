from flask import Blueprint, jsonify, abort, render_template
from flask_login import login_required, current_user
from app.models import Track, User, Album
from ..forms import TrackForm

track_routes = Blueprint('tracks', __name__)


@track_routes.route('/', methods=["GET"])
def get_all_tracks():
    """
    Query for all tracks and returns them in a list of track dictionaries
    """
    tracks = Track.query.all()
    return {'tracks': [track.to_dict() for track in tracks]}


@track_routes.route('/<int:track_id>', methods=["GET"])
def get_track_by_id(track_id):
    """
    Query for getting a track by track id and returning it is a dictionary
    """
    track = Track.query.get(track_id)

    if not track:
        response = jsonify({"message": "Track couldn't be found"})
        response.status_code = 404
        return response
    
    return track.to_dict()


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


@track_routes.route('/new', methods=["POST"])
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

        if form.validate_on_submit():
            pass

        return render_template('create_track.html', form=form)


    return user
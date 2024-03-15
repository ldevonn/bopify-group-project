from flask import Blueprint, jsonify, abort
from flask_login import login_required, current_user
from app.models import Track

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
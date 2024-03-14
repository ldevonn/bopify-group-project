from flask import Blueprint, jsonify, abort
from flask_login import login_required
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


# @track_routes.route('/<int:trackId>')
# @login_required
# def user(id):
#     """
#     Query for all tracks by current user (artist) by id and returns that user in a dictionary
#     """
#     user = User.query.get(id)
#     return user.to_dict()

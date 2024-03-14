from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Track

track_routes = Blueprint('tracks', __name__)


@track_routes.route('/')
def get_all_tracks():
    """
    Query for all tracks and returns them in a list of track dictionaries
    """
    tracks = Track.query.all()
    return {'tracks': [track.to_dict() for track in tracks]}

@track_routes.route('/<int:track_id>')
def get_track_by_id(track_id):
    track = Track.query.get(track_id).to_dict()
    return track


# @track_routes.route('/<int:trackId>')
# @login_required
# def user(id):
#     """
#     Query for all tracks by current user (artist) by id and returns that user in a dictionary
#     """
#     user = User.query.get(id)
#     return user.to_dict()

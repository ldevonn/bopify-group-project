from flask import Blueprint, jsonify, abort, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Track, db, Like, User, likes
from ..forms import TrackForm

likes_routes = Blueprint('likes', __name__)


@likes_routes.route('/', methods=["GET"])
@login_required
def get_all_liked_songs():
    """
    Query for all liked tracks by the logged in user
    """
    user_id = current_user.id

    liked_tracks = (
    db.session.query(Track)
    .join(Like, Like.c.track_id == Track.id)
    .filter(Like.c.user_id == user_id)
    .all()
    )

    return {'tracks': [track.to_dict() for track in liked_tracks]}


@likes_routes.route('/<int:track_id>', methods=["GET", "POST", "DELETE"])
def get_or_create_or_delete_like(track_id):
    """
    Query for 
    getting all likes by track id (GET) 
    OR creating a like by track id (PUT) 
    OR deleting a like by track id (DELETE)
    """
    track = Track.query.get(track_id)

    if not track:
        response = jsonify({"message": "Track couldn't be found"})
        response.status_code = 404
        return response
    
    if request.method in ["PUT", "DELETE"] and track.artist_id != current_user.id:
        return jsonify({"message": "Unauthorized access"}), 403
    
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
        

@likes_routes.route('/current', methods=["GET"])
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
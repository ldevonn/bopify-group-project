from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Track, db, Like
from sqlalchemy import delete

likes_routes = Blueprint('likes', __name__)


@likes_routes.route('/', methods=["GET"])
@login_required
def get_all_liked_songs():
    """
    Query for all liked tracks by the logged in user
    """
    user_id = current_user.id
    print("currentUser: ", current_user)
    print("<--------------LIKE ROUTE FUNCTION WAS CALLED! --------------------->")
    print("user_id: ", user_id)

    liked_tracks = (
    db.session.query(Track)
    .join(Like, Like.c.track_id == Track.id)
    .filter(Like.c.user_id == user_id)
    .all()
    )

    print("LIKED_TRACKS: ", liked_tracks)

    return {'tracks': [track.to_dict() for track in liked_tracks]}, 200


@likes_routes.route('/<int:track_id>', methods=["GET", "POST", "DELETE"])
def get_or_create_or_delete_like(track_id):
    """
    Query for 
    getting all likes by track id (GET) 
    OR creating a like by track id (PUT) 
    OR deleting a like by track id (DELETE)
    """
    track = Track.query.get(track_id)
    user_id = current_user.id

    if not track:
        response = jsonify({"message": "Track couldn't be found"})
        response.status_code = 404
        return response
    
    if request.method in ["POST", "DELETE"]:
        if not current_user.is_authenticated:
            return jsonify({"message": "Unauthorized access"}), 403
    
    if request.method == 'GET':
        likes = db.session.query(Like).filter(Like.c.track_id == track_id).all()
        return jsonify({'likes': len(likes)})
    
    if request.method == 'POST':
        check_like = db.session.query(Like).filter(Like.c.track_id == track_id, Like.c.user_id == user_id).first()
        if check_like:
            return jsonify({"message": "Like already exists"}), 400
        else:
            create_like = {"user_id": user_id, "track_id": track_id}
            db.session.execute(Like.insert(), create_like)
            db.session.commit()
            return jsonify({"message": "You have successfully liked the track"}), 201
        
    if request.method == 'DELETE':
        deleted_like_sql = delete(Like).where(
            Like.c.track_id == track_id,
            Like.c.user_id == user_id
        )
        result = db.session.execute(deleted_like_sql)
        db.session.commit()

        if result.rowcount > 0:
            return jsonify({"message": "Successfully Deleted Like"}), 200
        else:
            return jsonify({"message": "Like couldn't be found"}), 404
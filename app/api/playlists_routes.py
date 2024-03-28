from flask import Blueprint, jsonify, request
from app.models import Playlist, Track, User, db
from app.models.playlists_tracks import PlaylistsTracks
from app.forms.playlist_form import PlaylistForm

from flask_login import current_user, login_required

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/current')
@login_required
def get_current_user_playlists():
  """
  Query for a playlist populated by the current user from flask_login package
  """
  playlists = Playlist.query.filter(Playlist.user_id == current_user.id).all()
  playlist_data = [playlist.to_dict() for playlist in playlists]
  for data in playlist_data:
    tracks = Track.query.join(PlaylistsTracks).filter(PlaylistsTracks.c.playlist_id == data['id']).all()
    data["tracks"] = [track.to_dict() for track in tracks]

  return {'playlists': playlist_data}

@playlist_routes.route('/<int:playlist_id>', methods=["GET", "PUT", "DELETE"])
@login_required
def get_playlist_by_id(playlist_id):
  """
  Query for a playlist by id and returns that playlist in a dictionary including it's tracks
  OR Edit a playlist by id and returns the updated playlist in a dictionary including it's tracks
  OR Delete a playlist by id
  """

  playlist = Playlist.query.get(playlist_id)

  if not playlist:
    res = jsonify({"message": "Playlist couldn't be found"})
    res.status_code = 404
    return res
  
  if request.method in ["PUT", "DELETE"] and playlist.user_id != current_user.id:
    return jsonify({"message": "Unauthorized access"}), 403

  if request.method == "GET":
    tracks = Track.query.join(PlaylistsTracks).filter(PlaylistsTracks.columns.playlist_id == playlist_id).all()
    return {"playlist": 
              {
                "name": playlist.name, 
                "userId": playlist.user_id,
                "imageUrl": playlist.image_url,
                "Private": playlist.private,
                "tracks": [track.to_dict() for track in tracks]
              }
            }
  
  if request.method == "PUT":
    form = PlaylistForm(obj=playlist)

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
      playlist.name = form.name.data
      playlist.image_url = form.imageUrl.data
      playlist.private = form.private.data
      
      db.session.commit()

      tracks = Track.query.join(PlaylistsTracks).filter(PlaylistsTracks.columns.playlist_id == playlist_id).all()

      return {
              "name": playlist.name, 
              "userId": playlist.user_id,
              "imageUrl": playlist.image_url,
              "Private": playlist.private,
              "tracks": [track.to_dict() for track in tracks]
            }, 201

  if request.method == "DELETE":
    db.session.delete(playlist)
    db.session.commit()
    return jsonify({"message": "Successfully Deleted"})


@playlist_routes.route('/new', methods=["POST"])
@login_required
def create_playlist():
  """
  Create a playlist. A user or artist must be logged in.
  """
  user = User.query.get(current_user.id)
  if not user:
    return jsonify({"message": "User not found"}), 404
  
  form = PlaylistForm()
  
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    data = form.data
    new_playlist = Playlist(
                      name = data["name"],
                      image_url = data["imageUrl"],
                      user_id = current_user.id,
                      private = data["private"],
    )
    db.session.add(new_playlist)
    db.session.commit()
    playlist = Playlist.query.get(new_playlist.id).to_dict()
    return jsonify(playlist), 201
  else:
    return jsonify({"message": "Form validation errors", "errors": form.errors}), 400
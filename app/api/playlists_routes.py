from flask import Blueprint, jsonify
from app.models import Playlist, Track, PlaylistsTracks
from flask_login import current_user, login_required

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/current')
@login_required
def get_current_user_playlists():
  playlists = Playlist.query.filter(Playlist.user_id == current_user.id).all()
  return {'playlists': [playlist.to_dict() for playlist in playlists]}

@playlist_routes.route('/<int:playlist_id>')
def get_playlist_by_id(playlist_id):

  playlist = Playlist.query.get(playlist_id)
  tracks = Track.query.join(PlaylistsTracks.playlist_id)
  if not playlist:
    res = jsonify({"message": "Playlist couldn't be found"})
    res.status_code = 404
    return res
  

  
  return playlist.to_dict()
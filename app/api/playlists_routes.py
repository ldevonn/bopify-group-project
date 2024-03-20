from flask import Blueprint, jsonify
from app.models import Playlist, Track
from flask_login import current_user

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/')
def get_all_playlists():
  print(dir(current_user.to_dict()))
  playlists = Playlist.query.filter(Playlist.user_id == current_user.id).all()
  return {'playlists': [playlist.to_dict() for playlist in playlists]}

# @playlist_routes.route('/<int:playlist_id>')
# def get_playlist_by_id(playlist_id):
#   playlist = Playlist.query.get(playlist_id)
from flask import Blueprint, jsonify
from app.models import Playlist
from flask_login import current_user, login_user, logout_user, login_required

playlist_routes = Blueprint('playlists', __name__)

@playlist_routes.route('/')
def playlists():
  print(current_user.to_dict())
  pass


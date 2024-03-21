from flask import Blueprint, jsonify
from app.models import Playlist, Track
from app.models.playlists_tracks import PlaylistsTracks
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

@playlist_routes.route('/<int:playlist_id>')
def get_playlist_by_id(playlist_id):
  """
  Query for a playlist by id and returns that playlist in a dictionary including it's tracks
  """

  playlist = Playlist.query.get(playlist_id)
  tracks = Track.query.join(PlaylistsTracks).filter(PlaylistsTracks.columns.playlist_id == playlist_id).all()
  if not playlist:
    res = jsonify({"message": "Playlist couldn't be found"})
    res.status_code = 404
    return res
  
  return {"playlist": 
            {
              "name": playlist.name, 
              "userId": playlist.user_id,
              "imageUrl": playlist.image_url,
              "Private": playlist.private,
              "tracks": [track.to_dict() for track in tracks]
            }
          }
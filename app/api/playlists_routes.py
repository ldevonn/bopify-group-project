from flask import Blueprint, jsonify, request
from app.models import Playlist, Track, User, Album, db
from app.models.playlists_tracks import PlaylistsTracks
from app.forms.playlist_form import PlaylistForm
from app.forms.playlist_track_form import PlaylistTrackForm
from app.api.aws import (upload_file_to_s3, get_unique_filename, remove_file_from_s3)
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
    trackList = []
    for track in tracks:
        track_data = track.to_dict()

        artist = User.query.get(track_data['artistId'])
        track_data['artistName'] = artist.name

        album = Album.query.get(track_data['albumId']).to_dict()
        track_data['albumImage'] = album['imageUrl']

        trackList.append(track_data)

    user = User.query.get(playlist.user_id).to_dict()
    return {"playlist":
              {
                "name": playlist.name,
                "userId": playlist.user_id,
                "imageUrl": playlist.image_url,
                "Private": playlist.private,
                "user": user,
                "tracks": trackList
              }
            }

  if request.method == "PUT":
    form = PlaylistForm(obj=playlist)

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
      playlist.name = form.name.data
      playlist.private = form.private.data
      newImageUrl = form.imageUrl.data
      newImageUrl.filename = get_unique_filename(newImageUrl.filename)
      upload = upload_file_to_s3(newImageUrl)
      print(upload)

      if "url" not in upload:
        form.errors['image'][0] == 'File upload failed'

      url = upload["url"]

      playlist.image_url = url

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
    remove_file_from_s3(playlist.image_url)
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
    image = form.data["imageUrl"]
    image.filename = get_unique_filename(image.filename)
    upload = upload_file_to_s3(image)
    print(upload)

    if "url" not in upload:
      form.errors['image'][0] == 'File upload failed'

    url = upload["url"]

    new_playlist = Playlist(
                      name = data["name"],
                      image_url = url,
                      user_id = current_user.id,
                      private = data["private"],
    )
    db.session.add(new_playlist)
    db.session.commit()
    playlist = Playlist.query.get(new_playlist.id).to_dict()
    return jsonify(playlist), 201
  else:
    print(form.errors)
    return jsonify({"message": "Form validation errors", "errors": form.errors}), 400


@playlist_routes.route('<int:playlist_id>/tracks/<int:track_id>', methods=["POST"])
@login_required
def add_track_to_playlist(playlist_id, track_id):
  """
  Add a track to an existing playlist
  """
  playlist = Playlist.query.get(playlist_id)
  track = Track.query.get(track_id)
  if not playlist:
    return jsonify({"message": "Playlist not found"}), 404

  if playlist.user_id != current_user.id:
    return jsonify({"message": "Unauthorized access"}), 403

  if not track:
    return jsonify({"message": "Track not found"}), 404
  
  if track in playlist.tracks:
    return jsonify({"message": "Track is already in the playlist"}), 400
  
  put_track_in_playlist = {"track_id": track_id, "playlist_id": playlist_id}
  db.session.execute(PlaylistsTracks.insert(), put_track_in_playlist)
  db.session.commit()
  return jsonify({"message": "You have successfully added the track to playlist"}), 201


# @playlist_routes.route('/<int:playlist_id>/add-a-track', methods=['POST'])
# @login_required
# def add_track_to_playlist(playlist_id):
#   """
#   Add a track to an existing playlist
#   """
#   playlist = Playlist.query.get(playlist_id)

#   if not playlist:
#     return jsonify({"message": "Playlist not found"}), 404

#   if playlist.user_id != current_user.id:
#     return jsonify({"message": "Unauthorized access"}), 403

#   form = PlaylistTrackForm()

#   form['csrf_token'].data = request.cookies['csrf_token']
#   if form.validate_on_submit():
#     track_id = form.track_id.data
#     track = Track.query.get(track_id)

#     # print(form.errors)

#     if not track:
#       return jsonify({"message": "Track not found"}), 404

#     if track in playlist.tracks:
#       return jsonify({"message": "Track is already in the playlist"}), 400

#     playlist.tracks.append(track)
#     db.session.commit()

#     return jsonify({"message": "Track added to playlist successfully"}), 201

#   else:
#         errors = form.errors
#         return jsonify({"message": "Form validation errors", "errors": errors}), 400

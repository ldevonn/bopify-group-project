from app.models import db, Playlist, environment, SCHEMA
from sqlalchemy.sql import text
from app.api.aws import upload_file_to_s3, get_unique_filename, create_presigned_url


playlist_files = [
    {"path": "/Users/edwardjung/Pictures/Playlist1.jpeg", "user_id": 1, "name": "Rap", "private": False},
    {"path": "/Users/edwardjung/Pictures/Playlist2.jpeg", "user_id": 2, "name": "someone else", "private": True},
]

def seed_playlists():
    # for playlist_data in playlist_files:
    #     image_path = playlist_data["path"]

    #     try:
    #         with open(image_path, "rb") as image_file:
    #             filename = get_unique_filename(image_file.name)
    #             upload_result = upload_file_to_s3(image_file, filename)
    #             if not upload_result:
    #                 print(f"Error uploading playlist cover image {image_path}")
    #                 continue

    #             image_url = create_presigned_url(filename, expiration_seconds=157680000)

    #     except FileNotFoundError:
    #         print(f"Playlist file not found: {image_path}")
    #         continue

    #     playlist = Playlist(
    #         name=playlist_data["name"],
    #         image_url=image_url,
    #         user_id=playlist_data["user_id"],
    #         private=playlist_data["private"],
    #     )

    #     db.session.add(playlist)

    # db.session.commit()



    playlist1 = Playlist(
        name='Rap', user_id=1, image_url=
        'https://bopify-files.s3.us-west-1.amazonaws.com/Playlist1.jpeg',
        private=False)
    playlist2 = Playlist(
        name='someone else', user_id=2, image_url=
        'https://bopify-files.s3.us-west-1.amazonaws.com/Playlist2.jpeg',
        private=True)

    db.session.add(playlist1)
    db.session.add(playlist2)

    db.session.commit()


def undo_playlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))

    db.session.commit()

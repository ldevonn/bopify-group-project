from app.models import db, Track, environment, SCHEMA
from sqlalchemy.sql import text
from app.api.aws import upload_file_to_s3, get_unique_filename, create_presigned_url

track_files = [
    {"path": "/Users/edwardjung/Music/JohnMayer1.mp3", "name": "3x5", "duration": 289, "artist_id": 5, "album_id": 4},
    {"path": "/Users/edwardjung/Music/Track2.mp3", "name": "I Love Kanye", "duration": 186, "artist_id": 4, "album_id": 2},
    {"path": "/Users/edwardjung/Music/Track3.mp3", "name": "Lift Yourself", "duration": 147, "artist_id": 4, "album_id": 3},
    {"path": "/Users/edwardjung/Music/Track4.mp3", "name": "On The Run", "duration": 215, "artist_id": 3, "album_id": 1},
]


def seed_tracks():
    # for track_data in track_files:
    #     file_path = track_data["path"]

    #     try:
    #         with open(file_path, "rb") as track_file:
    #             filename = get_unique_filename(track_file.name)
    #             upload_result = upload_file_to_s3(track_file, filename)
    #             if not upload_result:
    #                 print(f"Error uploading track file {file_path}")
    #                 continue

    #             track_url = create_presigned_url(filename, expiration_seconds=157680000)

    #     except FileNotFoundError:
    #         print(f"Track file not found: {file_path}")
    #         continue

    #     track = Track(
    #         name=track_data["name"],
    #         duration=track_data["duration"],
    #         file=track_url,
    #         artist_id=track_data["artist_id"],
    #         album_id=track_data["album_id"],
    #     )

    #     db.session.add(track)

    # db.session.commit()





    # file1_track = open('/Users/edwardjung/Music/JohnMayer1.mp3', 'rb')
    # file1_track.filename = get_unique_filename(file1_track.name)
    # file2_track = open('/Users/edwardjung/Music/Track2.mp3', 'rb')
    # file2_track.filename = get_unique_filename(file2_track.name)
    # file3_track = open('/Users/edwardjung/Music/Track3.mp3', 'rb')
    # file3_track.filename = get_unique_filename(file3_track.name)
    # file4_track = open('/Users/edwardjung/Music/Track4.mp3', 'rb')
    # file4_track.filename = get_unique_filename(file4_track.name)

    # track1_upload = upload_file_to_s3(file1_track)
    # track2_upload = upload_file_to_s3(file2_track)
    # track3_upload = upload_file_to_s3(file3_track)
    # track4_upload = upload_file_to_s3(file4_track)

    # if "url" not in track1_upload or "url" not in track2_upload \
    #     or "url" not in track3_upload or "url" not in track4_upload:
    #     # Handle error case
    #     print("Error uploading files to S3")
    #     return

    track1 = Track(
        name='3x5', duration=289, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/JohnMayer1.mp3', 
        artist_id=5, album_id=4)
    track2 = Track(
        name='I Love Kanye', duration=44, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Track2.mp3', 
        artist_id=4, album_id=2)
    track3 = Track(
        name='Lift Yourself', duration=147, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Track3.mp3', 
        artist_id=4, album_id=3)
    track4 = Track(
        name='On The Run', duration=215, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Track4.mp3', 
        artist_id=3, album_id=1)



    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)
    db.session.add(track4)
    db.session.commit()

    # file1_track.close()
    # file2_track.close()
    # file3_track.close()
    # file4_track.close()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_tracks():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.tracks RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM tracks"))

    db.session.commit()

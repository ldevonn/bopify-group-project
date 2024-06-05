from app.models import db, Album, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date
from app.api.aws import upload_file_to_s3, get_unique_filename, create_presigned_url


album_files = [
    {"path": "/Users/edwardjung/Pictures/AlbumImage1.jpeg", "name": "The Dark Side of the Moon", "release_date": date(1973,3,1), "album_type": 'album', "genre": 'rock', "artist_id": 3},
    {"path": "/Users/edwardjung/Pictures/AlbumImage2.jpeg", "name": "The Life of Pablo", "release_date": date(2016,2,14), "album_type": 'album', "genre": 'hiphop', "artist_id": 4},
    {"path": "/Users/edwardjung/Pictures/AlbumImage3.jpeg", "name": "Lift Yourself", "release_date": date(2018,4,29), "album_type": 'single', "genre": 'hiphop', "artist_id": 4},
    {"path": "/Users/edwardjung/Pictures/AlbumImage4.jpeg", "name": "Room for Squares", "release_date": date(2001,8,16), "album_type": 'album', "genre": 'pop', "artist_id": 5},
]

# Adds a demo user, you can add other users here if you want
def seed_albums():
    # for album_data in album_files:
    #     file_path = album_data["path"]

    #     try:
    #         with open(file_path, "rb") as album_file:
    #             filename = get_unique_filename(album_file.name)
    #             upload_result = upload_file_to_s3(album_file, filename)
    #             if not upload_result:
    #                 print(f"Error uploading album image {file_path}")
    #                 continue

    #             album_url = create_presigned_url(filename, expiration_seconds=157680000)

    #     except FileNotFoundError:
    #         print(f"Album file not found: {file_path}")
    #         continue

    #     album = Album(
    #         name=album_data["name"],
    #         release_date=album_data["release_date"],
    #         image_url=album_url,
    #         album_type=album_data["album_type"],
    #         genre=album_data["genre"],
    #         artist_id=album_data["artist_id"]
    #     )

    #     db.session.add(album)

    # db.session.commit()






    album1 = Album(
        name='The Dark Side of the Moon', release_date=date(1973,3,1), album_type='album', image_url=
        'https://bopify-files.s3.us-west-1.amazonaws.com/Dark_Side_Of_Moon.jpg', 
        genre='rock', artist_id=3)
    album2 = Album(
        name='The Life of Pablo', release_date=date(2016,2,14), album_type='album', image_url=
        'https://bopify-files.s3.us-west-1.amazonaws.com/Life_Of_Pablo.jpg', 
        genre='hiphop', artist_id=4)
    album3 = Album(
        name='Lift Yourself', release_date=date(2018,4,29), album_type='single', image_url=
        'https://bopify-files.s3.us-west-1.amazonaws.com/Life_Yourself.jpg', 
        genre='hiphop', artist_id=4)
    album4 = Album(
        name='Room for Squares', release_date=date(2001,8,16), album_type='album', image_url=
        'https://bopify-files.s3.us-west-1.amazonaws.com/Room_For_Squares.jpg', 
        genre='pop', artist_id=5)

    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))

    db.session.commit()

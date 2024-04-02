from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from app.api.aws import upload_file_to_s3, get_unique_filename, create_presigned_url

user_files = [
    {"path": "/Users/edwardjung/Pictures/profile1.jpg", "name": "Demo-lition", "email": "demo@gmail.com", "password": "password", "is_artist": False},
    {"path": "/Users/edwardjung/Pictures/profile2.jpg", "name": "Demo-lition2", "email": "demo2@gmail.com", "password": "password", "is_artist": False},
    {"path": "/Users/edwardjung/Pictures/profile3.jpg", "name": "Pink Floyd", "email": "pinkfloyd@gmail.com", "password": "password", "is_artist": True},
    {"path": "/Users/edwardjung/Pictures/profile4.jpg", "name": "Ye", "email": "ye@yeye.com", "password": "password", "is_artist": False},
    {"path": "/Users/edwardjung/Pictures/profile5.jpg", "name": "John Mayer", "email": "john@mayer.com", "password": "password", "is_artist": True},
]

# Adds a demo user, you can add other users here if you want
def seed_users():
    # for user_data in user_files:
    #     image_path = user_data["path"]

    #     try:
    #         with open(image_path, "rb") as image_file:
    #             filename = get_unique_filename(image_file.name)
    #             upload_result = upload_file_to_s3(image_file, filename)
    #             if not upload_result:
    #                 print(f"Error uploading user image {image_path}")
    #                 continue

    #             image_url = create_presigned_url(filename, expiration_seconds=157680000)

    #     except FileNotFoundError:
    #         print(f"User file not found: {image_path}")
    #         continue

    #     user = User(
    #         name=user_data["name"],
    #         email=user_data["email"],
    #         image_url=image_url,
    #         password=user_data["password"],
    #         is_artist=user_data["is_artist"],
    #     )

    #     db.session.add(user)

    # db.session.commit()
    
    




    user1 = User(
        name='Demo-lition', email='demo@gmail.com', password='password', is_artist=False)
    user2 = User(
        name='Demo-lition2', email='demo2@gmail.com', password='password', is_artist=False)
    user3 = User(
        name='Pink Floyd', email='pinkfloyd@gmail.com', password='password', image_url=
        "https://s3.us-west-1.amazonaws.com/my.spotify.music/profile1.jpg", 
        is_artist=True)
    user4 = User(
        name='Ye', email='ye@yeye.com', password='yeyeye', image_url=
        "https://s3.us-west-1.amazonaws.com/my.spotify.music/profile2.jpg", 
        is_artist=False)
    user5 = User(
        name='John Mayer', email='john@mayer.com', password='password', image_url=
        "https://s3.us-west-1.amazonaws.com/my.spotify.music/profile3.jpg", 
        is_artist=True)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()

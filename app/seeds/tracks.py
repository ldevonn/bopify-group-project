from app.models import db, Track, environment, SCHEMA
from sqlalchemy.sql import text
from app.api.aws import upload_file_to_s3, get_unique_filename


def seed_tracks():
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
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/JohnMayer1.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T235128Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=a2bf25c6e3591a3adc467769f37eecf5f22ec47d04ae3da41d66ee7c5529ee9b', 
        artist_id=5, album_id=4)
    track2 = Track(
        name='I Love Kanye', duration=44, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/JohnMayer1.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T235128Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=a2bf25c6e3591a3adc467769f37eecf5f22ec47d04ae3da41d66ee7c5529ee9b', 
        artist_id=4, album_id=2)
    track3 = Track(
        name='Lift Yourself', duration=147, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/JohnMayer1.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T235128Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=a2bf25c6e3591a3adc467769f37eecf5f22ec47d04ae3da41d66ee7c5529ee9b', 
        artist_id=4, album_id=3)
    track4 = Track(
        name='On The Run', duration=215, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/JohnMayer1.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T235128Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=a2bf25c6e3591a3adc467769f37eecf5f22ec47d04ae3da41d66ee7c5529ee9b', 
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

from app.models import db, Playlist, environment, SCHEMA
from sqlalchemy.sql import text


def seed_playlists():
    playlist1 = Playlist(
        name='Rap', user_id=1, image_url=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Playlist1.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T172806Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=f75c5f13749bffa09d8a1c597800869425830cccee7fbc92b08f9d8251166f5a', 
        private=False)
    playlist2 = Playlist(
        name='someone else', user_id=2, image_url=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Playlist2.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T172836Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=bfcf825216327dc6114e0f6d6fab2daf2b6e32e43b6f148ef53b9518683565d8', 
        private=True)



    db.session.add(playlist1)
    db.session.add(playlist2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_playlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))

    db.session.commit()

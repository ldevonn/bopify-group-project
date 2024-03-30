from app.models import db, Album, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


# Adds a demo user, you can add other users here if you want
def seed_albums():
    album1 = Album(
        name='The Dark Side of the Moon', release_date=date(1973,3,1), album_type='album', image_url=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/AlbumImage1.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T164906Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=4268493d01404e92ffb61f7764981a689f75b2fb2f2516ee475d02a94b537351', 
        genre='rock', artist_id=3)
    album2 = Album(
        name='The Life of Pablo', release_date=date(2016,2,14), album_type='album', image_url=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/AlbumImage4.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T164809Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=ecfc8c70591671017c719a2c09fe1d93e41d6ecaf5278b0d030f428f8ad3259a', 
        genre='hiphop', artist_id=4)
    album3 = Album(
        name='Lift Yourself', release_date=date(2018,4,29), album_type='single', image_url=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/AlbumImage2.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T164853Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=66dd75de4a7321c60828e7900d8ee19c5d516cc277de2d645d57ce12b2936f1a', 
        genre='hiphop', artist_id=4)
    album4 = Album(
        name='Room for Squares', release_date=date(2001,8,16), album_type='album', image_url=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/AlbumImage3.jpeg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T164834Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=4c2e7ed5b787f8f14d2255843231d2ab85863b92f34d45f345b1e78b138451f7', 
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

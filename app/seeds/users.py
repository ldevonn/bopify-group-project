from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    user1 = User(
        name='Demo-lition', email='demo@gmail.com', password='password', is_artist=False)
    user2 = User(
        name='Demo-lition2', email='demo2@gmail.com', password='password', is_artist=False)
    user3 = User(
        name='Pink Floyd', email='pinkfloyd@gmail.com', password='password', image_url=
        "https://s3.us-west-1.amazonaws.com/my.spotify.music/Profile2-ezgif.com-webp-to-jpg-converter.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T172119Z&X-Amz-SignedHeaders=host&X-Amz-Expires=299&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=480189e819a7b7868148f722ccd264a491200ea52797252fc90a75e2ad6f2b38", 
        is_artist=True)
    user4 = User(
        name='Ye', email='ye@yeye.com', password='yeyeye', image_url=
        "https://s3.us-west-1.amazonaws.com/my.spotify.music/Profile3-ezgif.com-webp-to-jpg-converter.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T172142Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=e2bcc72cc5148bf8b77097aa7036f596e804d71055f5aa0963de07571f2712a4", 
        is_artist=False)
    user5 = User(
        name='John Mayer', email='john@mayer.com', password='password', image_url=
        "https://s3.us-west-1.amazonaws.com/my.spotify.music/profile1.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJHMEUCIEy1qmJR5KZhKJoHBcFnGJjfH3phxw%2F73khNtNdk7IJgAiEAnXfi8hPDAJ8m06H9PZbb4C%2F5oaxWieWIYQXpdnSTlngq5AIIGBAAGgwyMTExMjU0NzU5MTAiDGfqfubU5d83aYAQnirBAkC5c7vcScIneKmjS6lGL1zjyzUle1fV3JUFeyjWLo7C3zTcPlhapqLbMlaxnie0vEvD%2BsRVc%2FDeJztlcwY3kgExVsfew%2FFuSvmhmNsTapla8YUjUHMPAJXGApS9v8MiYZc2y6PH5MFekPmoxQSMv3QNkc7%2BeVmIrDdWpFQHEVwBmy6JcYlunfz4LPnZ%2B5F5G3Iz9c9mrHGOEJ0h9kMKqdXZ1Jg%2FhlSmc%2BClhWTLmWaHxgMW%2B2DzT3wPbKnzHUvn4OgjzCx32AK3Jbie9SfjyYElpNGTqMXNeghVy8Z2vPM8Q8gtYnDfhW8ZxdyHcroakBoDFFUS22UbprcxMFUgtL4qf3Mq%2FeTX8StclXvryQ0Equs5UdI%2FpAhKeeedxCnewW6l6I2a4aqhBJKDecCMM7uX3rUrmaN9BAnNKuK9%2F7NZNjCk06CwBjqzAtrmDysbykCxEdB55poo15F4dMP9KeODuh50FNh%2Bx3VlIyrWGTv94%2BELf6zDKVxFCYrYuf11x0HJcoI0xOg6to2xF%2FOKQ%2F5SnRU%2Fg08p6pBC%2BndrNLqhBPtC6Zvj93f%2BIYrev%2FIkW1O25DEgxwuSZNNlXpbaK589qerrrbgydHjBDkWBwNq91kPaWTuMny2T8uttIsc1%2BXyDjmtswcYrfmKCvkyEHaBiL0h6xp%2Fwrgp7Pf1JfbMgfDbOWa%2FLx2RVhv2sc80bZd6FM1BIuupEN89o3METBYZpXdYkPhrFBITuDtWYtKa6PPZJ%2Fy34r45bJ04NFegC9VizZEyOnR4UrexDYpoYIpa9RPl1pnNZ%2BxNYsD3Xnh5AoQqpl%2FM%2FG4xzuTHLgaPgRRhgvyljVQ7S43aTDsI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240330T172102Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDNNTCQAFJ%2F20240330%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=11dd00129384f04928a2ce8c65f4d4084f38a3f5067c778dd00b7e56c1982fb3", 
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

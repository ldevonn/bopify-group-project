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
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/JohnMayer1.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJIMEYCIQDWeo2BuUrWE4ZXfpga%2FeVblcGbXY%2FHovTiX7P10gR5BQIhAONSFCi1iHLHPoRn8bdPymDN2Z0FOPJZSXR0Zk3f%2FD13Ku0CCOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMjExMTI1NDc1OTEwIgzJq%2F%2FhQUS2c3LtEvUqwQKINY3esUebUdn%2FbqKB%2B0mF2zBHGePBNCTViLTZLH8Cr2c7%2FjhCNE%2BLQTon0%2FO0v0y5LIMriUBapCN4372s9VGvS55sJRcYukI5hYJUbW%2Bo1mj33Kt9c6G%2BAsrzXvd3r3dJkSYGlJXBRC5xZq12Tef6w%2BM%2BMYrhzGcIeMz0GFdnjfkvE%2Feer9YT8t3hSH7s3niNrf6RKaUHtftLjrQWDnWxRXASJHU5S8bl9WYEElZRLjUyDyHvN2aDLlucit1O7v8pXX2gibHdVUUmAxwvBLUKOpx%2FospPo7gdVwBxX3D47%2BNma1JbQBYJm8YNhripX8bLGytdtxF%2BAj7%2BpuO%2Fe2LlHSQRdNL91UMb60zOYtBd8N6W8N21fcMBuYQURwWpTCvLH9RGTbCOpBVkH21RZtf4vhRvrRBgdTPGBCYNSOldx6sw2s2YsAY6sgJQH0Vco4tNxR%2BsVjNeC57cyu2CupGAgIzpyMPhNqAAIF02mjKdb56Ktn6CTCuRTtE%2BFFkMcdczkq%2FZCAQDwur6FytLixH6T%2FV70tDMusnJmiIhrj2TipxS7vtUwWo6DnF4TkDi5tnhOrKzH9wZAKxytUzue7aYblLCLFOBAc5k9MExSFN2%2FAd87a94ll%2FuySdFyIp%2BAvEFilpKAytJxDpvuZIIqmAhy1KXWU20aG3lW%2BKSC8GrRa0IvGVccClLIZCYfZArixtTIGDHZnHas6eyoyAXW7rRmnxuksswdfcaIHXjwChQuIORBmn3NmULo76fp3SFPpDh63BGeYAVkCO3CmJ8iwppMmO%2FPn7%2BEKi8sC2Yww1pL1zYGjXQk%2BtsSI%2BsPK9G%2F7ZYu7C3Y0DuOMrb%2By4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240329T050839Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDP74RUYZQ%2F20240329%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=9438609f4da78c3d8d2b13bd13214cd5f811a73fe8f1087bf1a0dd73d08c9117', 
        artist_id=5, album_id=4)
    track2 = Track(
        name='I Love Kanye', duration=44, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Track2.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJIMEYCIQDWeo2BuUrWE4ZXfpga%2FeVblcGbXY%2FHovTiX7P10gR5BQIhAONSFCi1iHLHPoRn8bdPymDN2Z0FOPJZSXR0Zk3f%2FD13Ku0CCOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMjExMTI1NDc1OTEwIgzJq%2F%2FhQUS2c3LtEvUqwQKINY3esUebUdn%2FbqKB%2B0mF2zBHGePBNCTViLTZLH8Cr2c7%2FjhCNE%2BLQTon0%2FO0v0y5LIMriUBapCN4372s9VGvS55sJRcYukI5hYJUbW%2Bo1mj33Kt9c6G%2BAsrzXvd3r3dJkSYGlJXBRC5xZq12Tef6w%2BM%2BMYrhzGcIeMz0GFdnjfkvE%2Feer9YT8t3hSH7s3niNrf6RKaUHtftLjrQWDnWxRXASJHU5S8bl9WYEElZRLjUyDyHvN2aDLlucit1O7v8pXX2gibHdVUUmAxwvBLUKOpx%2FospPo7gdVwBxX3D47%2BNma1JbQBYJm8YNhripX8bLGytdtxF%2BAj7%2BpuO%2Fe2LlHSQRdNL91UMb60zOYtBd8N6W8N21fcMBuYQURwWpTCvLH9RGTbCOpBVkH21RZtf4vhRvrRBgdTPGBCYNSOldx6sw2s2YsAY6sgJQH0Vco4tNxR%2BsVjNeC57cyu2CupGAgIzpyMPhNqAAIF02mjKdb56Ktn6CTCuRTtE%2BFFkMcdczkq%2FZCAQDwur6FytLixH6T%2FV70tDMusnJmiIhrj2TipxS7vtUwWo6DnF4TkDi5tnhOrKzH9wZAKxytUzue7aYblLCLFOBAc5k9MExSFN2%2FAd87a94ll%2FuySdFyIp%2BAvEFilpKAytJxDpvuZIIqmAhy1KXWU20aG3lW%2BKSC8GrRa0IvGVccClLIZCYfZArixtTIGDHZnHas6eyoyAXW7rRmnxuksswdfcaIHXjwChQuIORBmn3NmULo76fp3SFPpDh63BGeYAVkCO3CmJ8iwppMmO%2FPn7%2BEKi8sC2Yww1pL1zYGjXQk%2BtsSI%2BsPK9G%2F7ZYu7C3Y0DuOMrb%2By4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240329T051036Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDP74RUYZQ%2F20240329%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=22b5053412e044776d2cedf85112843c2139094351fd1281add23d23bd2b1ea0', 
        artist_id=4, album_id=2)
    track3 = Track(
        name='Lift Yourself', duration=147, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Track3.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJIMEYCIQDWeo2BuUrWE4ZXfpga%2FeVblcGbXY%2FHovTiX7P10gR5BQIhAONSFCi1iHLHPoRn8bdPymDN2Z0FOPJZSXR0Zk3f%2FD13Ku0CCOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMjExMTI1NDc1OTEwIgzJq%2F%2FhQUS2c3LtEvUqwQKINY3esUebUdn%2FbqKB%2B0mF2zBHGePBNCTViLTZLH8Cr2c7%2FjhCNE%2BLQTon0%2FO0v0y5LIMriUBapCN4372s9VGvS55sJRcYukI5hYJUbW%2Bo1mj33Kt9c6G%2BAsrzXvd3r3dJkSYGlJXBRC5xZq12Tef6w%2BM%2BMYrhzGcIeMz0GFdnjfkvE%2Feer9YT8t3hSH7s3niNrf6RKaUHtftLjrQWDnWxRXASJHU5S8bl9WYEElZRLjUyDyHvN2aDLlucit1O7v8pXX2gibHdVUUmAxwvBLUKOpx%2FospPo7gdVwBxX3D47%2BNma1JbQBYJm8YNhripX8bLGytdtxF%2BAj7%2BpuO%2Fe2LlHSQRdNL91UMb60zOYtBd8N6W8N21fcMBuYQURwWpTCvLH9RGTbCOpBVkH21RZtf4vhRvrRBgdTPGBCYNSOldx6sw2s2YsAY6sgJQH0Vco4tNxR%2BsVjNeC57cyu2CupGAgIzpyMPhNqAAIF02mjKdb56Ktn6CTCuRTtE%2BFFkMcdczkq%2FZCAQDwur6FytLixH6T%2FV70tDMusnJmiIhrj2TipxS7vtUwWo6DnF4TkDi5tnhOrKzH9wZAKxytUzue7aYblLCLFOBAc5k9MExSFN2%2FAd87a94ll%2FuySdFyIp%2BAvEFilpKAytJxDpvuZIIqmAhy1KXWU20aG3lW%2BKSC8GrRa0IvGVccClLIZCYfZArixtTIGDHZnHas6eyoyAXW7rRmnxuksswdfcaIHXjwChQuIORBmn3NmULo76fp3SFPpDh63BGeYAVkCO3CmJ8iwppMmO%2FPn7%2BEKi8sC2Yww1pL1zYGjXQk%2BtsSI%2BsPK9G%2F7ZYu7C3Y0DuOMrb%2By4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240329T051149Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDP74RUYZQ%2F20240329%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=355116b18452d43aa55efbdceb77bf3843c1c2226f626a450240c76bbb9ccfd3', 
        artist_id=4, album_id=3)
    track4 = Track(
        name='On The Run', duration=215, file=
        'https://s3.us-west-1.amazonaws.com/my.spotify.music/Track4.mp3?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMSJIMEYCIQDWeo2BuUrWE4ZXfpga%2FeVblcGbXY%2FHovTiX7P10gR5BQIhAONSFCi1iHLHPoRn8bdPymDN2Z0FOPJZSXR0Zk3f%2FD13Ku0CCOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMjExMTI1NDc1OTEwIgzJq%2F%2FhQUS2c3LtEvUqwQKINY3esUebUdn%2FbqKB%2B0mF2zBHGePBNCTViLTZLH8Cr2c7%2FjhCNE%2BLQTon0%2FO0v0y5LIMriUBapCN4372s9VGvS55sJRcYukI5hYJUbW%2Bo1mj33Kt9c6G%2BAsrzXvd3r3dJkSYGlJXBRC5xZq12Tef6w%2BM%2BMYrhzGcIeMz0GFdnjfkvE%2Feer9YT8t3hSH7s3niNrf6RKaUHtftLjrQWDnWxRXASJHU5S8bl9WYEElZRLjUyDyHvN2aDLlucit1O7v8pXX2gibHdVUUmAxwvBLUKOpx%2FospPo7gdVwBxX3D47%2BNma1JbQBYJm8YNhripX8bLGytdtxF%2BAj7%2BpuO%2Fe2LlHSQRdNL91UMb60zOYtBd8N6W8N21fcMBuYQURwWpTCvLH9RGTbCOpBVkH21RZtf4vhRvrRBgdTPGBCYNSOldx6sw2s2YsAY6sgJQH0Vco4tNxR%2BsVjNeC57cyu2CupGAgIzpyMPhNqAAIF02mjKdb56Ktn6CTCuRTtE%2BFFkMcdczkq%2FZCAQDwur6FytLixH6T%2FV70tDMusnJmiIhrj2TipxS7vtUwWo6DnF4TkDi5tnhOrKzH9wZAKxytUzue7aYblLCLFOBAc5k9MExSFN2%2FAd87a94ll%2FuySdFyIp%2BAvEFilpKAytJxDpvuZIIqmAhy1KXWU20aG3lW%2BKSC8GrRa0IvGVccClLIZCYfZArixtTIGDHZnHas6eyoyAXW7rRmnxuksswdfcaIHXjwChQuIORBmn3NmULo76fp3SFPpDh63BGeYAVkCO3CmJ8iwppMmO%2FPn7%2BEKi8sC2Yww1pL1zYGjXQk%2BtsSI%2BsPK9G%2F7ZYu7C3Y0DuOMrb%2By4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240329T051234Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATCKAPDJDP74RUYZQ%2F20240329%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Signature=ecd8e28a29a40c1eb581812f59fb0815eecbf52057eed2826cdee32d5531b2ba', 
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

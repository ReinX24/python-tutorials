def make_album(artist_name, album_title, no_of_songs=None):
    if no_of_songs:
        return {'name': artist_name, 'album': album_title, 'song_amount': no_of_songs}
    else:
        return {'name': artist_name, 'album': album_title}


# print(make_album('juan karlos', 'diwa'))
# print(make_album('beabadoobee', 'beatopia', 14))
# print(make_album('huey lewis and the news', 'fore!', 11))

# Accepting user input using a while loop
while True:
    print("\nArtist and Album Recorder")
    print("(Enter 'q' anywhere to quit)")

    name = input("\nEnter artist name: ")
    if name == 'q':
        break

    album = input("Enter album: ")
    if album == 'q':
        break

    print(make_album(name, album))

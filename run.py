import spot
import youtu
import json


def get_artists_playlists():
    name = input("Enter artist's name: ")
    get_playlists(spotify.get_playlist_artist(name), name)


def get_user_playlists():
    user = input("Enter user: ")
    get_playlists(spotify.get_playlist_user(user), user)


def get_playlists(data, user):
    dirname = input("Enter dirname: ")
    i = 0
    for item in data:
        print(i, item["playlist_name"])
        i = i+1

    playlist = int(input("Which playlist do you want to download? "))
    playlist = data[playlist]
    print("Dowland ", playlist["playlist_name"])
    tracks = spotify.get_tracks_playlist(playlist["uri"], user)
    tracks = spotify.list_for_search(tracks)

    you = youtu.Youtu(dirname)
    for track in tracks:
        you.search_dowland(track)

print("1 User's playlists")
print("2 Artist's albums ")
print("3 Playlist Uri")

dictionary = {1: get_user_playlists, 2: get_artists_playlists}

spotify = spot.Spot()
try:
    inp = int(input("Enter option: "))
    dictionary[inp]()
except ValueError:
    print("Error")
except KeyError:
    print("Index error")

import spot
import youtu
import json
user = input("Enter the username: ")
dirname = input("Enter dirname: ")
spotify = spot.Spot(user)
data = spotify.get_playlist_user()
playlist = data[0]['uri']
print(playlist)
tracks = spotify.get_tracks_playlist(playlist)
tracks = spotify.list_for_search(tracks)

you = youtu.Youtu(dirname)
for track in tracks:
    you.search_dowland(track)

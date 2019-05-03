import spot
import youtu
import json
user = input("Enter the username: ")
dirname = input("Enter dirname: ")
spotify = spot.Spot(user)
data = spotify.get_playlist_user()

i = 0
for item in data:
    print(i, item["playlist_name"])
    i = i+1

playlist = int(input("Which playlist do you want to download? "))
playlist = data[playlist]
print("Dowland ", playlist["playlist_name"])
tracks = spotify.get_tracks_playlist(playlist["uri"])
tracks = spotify.list_for_search(tracks)

you = youtu.Youtu(dirname)
for track in tracks:
    you.search_dowland(track)

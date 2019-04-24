import spot
import json
user = input("Enter the username : ")

test = spot.Spot(user)
data = test.get_playlist_user()
playlist = data[0]['uri']
tracks = test.get_tracks_playlist(playlist)

list_search = test.list_for_search(tracks)
for pepe in list_search:
    print(pepe)
# print(json.dumps(tracks, indent=2))

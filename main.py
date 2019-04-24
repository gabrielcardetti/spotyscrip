
import spotipy
import spotipy.oauth2 as oauth2
import json
from private import *


class Spot(object):
    def __init__(self, username):
        # I'm not sure what parameters I need
        self.token = self.get_token()
        self.username = username
        self.sp = spotipy.Spotify(auth=self.token)
        # self.playlist = playlist ???

    def get_token(self):
        credentials = oauth2.SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_PRIVATE)
        token = credentials.get_access_token()
        return token

    def get_playlist_user(self):
        """
        I think I should return something like this.
        array of objects ??
       [ {
            playlist_name: //
            uri:
            image:[...]
        }....]
        """
        result = []
        playlists = self.sp.user_playlists(self.username)
        while playlists:
            for playlist in playlists['items']:
                data = {}
                data["playlist_name"] = playlist["name"]
                data["uri"] = playlist["uri"]
                data["images"] = playlist["images"]
                result.append(data)
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None
        return result

    def get_tracks_playlist(self, playlist_id):
        """
        [{
            {
            track_name:
            artist:
            album_name:
            images:
            }
        } ... ]

         *Features: limit of tracks
        """
        results = self.sp.user_playlist_tracks(self.username, playlist_id)
        tracks = results['items']
        # Loops to ensure I get every track of the playlist
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])
        result = []
        for track in tracks:
            data = {}
            data["track_name"] = track["track"]["name"]
            data["artist"] = track["track"]["album"]["artists"][0]["name"]
            data["album_name"] = track["track"]["album"]["name"]
            data["images"] = track["track"]["album"]["images"]
            result.append(data)
        return result

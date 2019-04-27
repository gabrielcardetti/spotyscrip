import spotipy
import spotipy.oauth2 as oauth2
import json
from private import *


class Spot(object):
    def __init__(self, username):
        self.username = username
        self.token = self.get_token()
        self.sp = spotipy.Spotify(auth=self.token)

    def get_token(self):
        credentials = oauth2.SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_PRIVATE
        )
        return credentials.get_access_token()

    def get_playlist_user(self):
        """
        Returns a map of playlists
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
                playlists = self.sp.next(playlists)
            else:
                playlists = None
        return result

    def get_tracks_playlist(self, playlist_id):
        """
        Returns an array of the tracks
        belonging to a certain playlist
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

    def list_for_search(self, tracks):
        """
        Build the search commands for youtube
        """
        result = []
        for track in tracks:
            path = track["track_name"] + " " + track["artist"]
            result.append(path)
        return result

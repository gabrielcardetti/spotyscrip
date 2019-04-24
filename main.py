
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
            name:
            uri:
            image:[...]
        }....]
        """
        result = []
        playlists = self.sp.user_playlists(self.username)
        while playlists:
            for playlist in playlists['items']:
                data = {}
                data["name"] = playlist["name"]
                data["uri"] = playlist["uri"]
                data["images"] = playlist["images"]
                result.append(data)
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None
        return result

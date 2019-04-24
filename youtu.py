from __future__ import unicode_literals 
from bs4 import BeautifulSoup
import youtube_dl
import urllib.request

class Youtu(object):
    def __init__(self):
        self.song_dowland = ""
    def search_dowland(self, querys):
        """
        ...
        """
        uri = self.search_track(querys)
        self.song_dowland = querys
        try:
            self.dowland_mp3(uri)
        except:
            print("ERROR DOWLAND")


    def search_track(self, querys):
        """
        https://stackoverflow.com/questions/29069444/returning-the-urls-as-a-list-from-a-youtube-search-query
        """
        textToSearch = querys
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            return('https://www.youtube.com' + vid['href'])


    def dowland_mp3(self, uri):
        """
            TODO: I should rename de files
        """
        print("[START DOWNLOAD] " + self.song_dowland+ "\r\n") 
        ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',}],
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                uri)
            # print(info['formats'][0]['url'])
        print("[COMPLETE DOWNLOAD] \r\n") 
        
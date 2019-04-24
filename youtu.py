from __future__ import unicode_literals 
import youtube_dl

class Youtu(object):

    def dowland_mp3(self, uri):
        """
            TODO: I should rename de files
        """
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
            print(info['formats'][0]['url'])
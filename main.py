from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import spot
import youtu

Builder.load_file('main.kv')


class TestApp(FloatLayout):
    def download(self, user, dirname):
        spotify = spot.Spot(user)
        data = spotify.get_playlist_user()
        playlist = data[0]['uri']
        print(playlist)
        tracks = spotify.get_tracks_playlist(playlist)
        tracks = spotify.list_for_search(tracks)
        you = youtu.Youtu(dirname)
        for track in tracks:
            you.search_dowland(track)

    def do(self):
        dir_name = self.ids.dirname.text
        user_name = self.ids.username.text
        self.download(user_name, dir_name)


class TApp(App):
    def build(self):
        return TestApp()

if __name__ == '__main__':
    TApp().run()

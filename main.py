from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder

Builder.load_file('main.kv')

class TestApp(AnchorLayout):
    def do(self):
        print(self.ids.txt_inp.text)

class TApp(App):
    def build(self):
        return TestApp()

if __name__ == '__main__':
    TApp().run()

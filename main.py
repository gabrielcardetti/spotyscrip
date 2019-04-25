from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
res = Builder.load_file('pepe.kv')


class TestHelp(Widget):
    pass


class TestApp(App):
    def build(self):
        return res


if __name__ == '__main__':
    TestApp().run()

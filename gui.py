from kivy.app import App
from kivy.uix.button import Button


class KivyButton(App):

    def build(self):
        bt = Button(text="Welcome to LikeGeeks!",
                    pos=(300, 350),
                    size_hint=(.25, .18))
        return bt


KivyButton().run()

from kivy.uix.screenmanager import ScreenManager, SlideTransition


class ScreenManagement(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def main(self):
        self.current = "main"

    def corrector(self):
        self.current = "corrector"

    def author(self):
        self.current = "author"

    def back(self):
        self.transition = SlideTransition(direction="right")
        self.main()
        self.transition = SlideTransition(direction="left")
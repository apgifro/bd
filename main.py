from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


class MainScreen(Screen):

    Builder.load_file("view/main.kv")


class NewScreen(Screen):

    Builder.load_file("view/new.kv")


class EditScreen(Screen):

    Builder.load_file("view/edit.kv")


class ScreenManagement(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def main_screen(self):
        self.current = "main"

    def new_screen(self):
        self.current = "new"

    def edit_screen(self):
        self.current = "edit"


class CBBD(MDApp):

    def build(self):
        Builder.load_file("view/management.kv")
        self.root = ScreenManagement()
        return self.root


if __name__ == '__main__':
    CBBD().run()
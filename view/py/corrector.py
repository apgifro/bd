from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class CorrectorScreen(Screen):
    Builder.load_file("view/src/corrector.kv")
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class ArticleScreen(Screen):
    Builder.load_file("view/src/article.kv")
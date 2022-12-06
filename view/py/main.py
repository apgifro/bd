from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.tab import MDTabsBase


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MainScreen(Screen):

    def __init__(self, **kw):
        self.data = {
            'Revisor': ["account", "on_press", self.corrector],
            'Artigo': ["book-open-page-variant-outline", "on_press", self.article]
        }
        Builder.load_file("view/src/main.kv")
        super().__init__(**kw)

    def on_enter(self):
        ids = self.manager.get_screen("main").ids
        self.list_corrector = ids.revisores.ids.list
        self.list_article = ids.artigos.ids.list
        self.list_corrector.add_widget(OneLineListItem(text="Clique no + para adicionar um revisor"))
        self.list_article.add_widget(OneLineListItem(text="Clique no + para adicionar um artigo"))


    def corrector(self, button):
        self.manager.corrector()

    def article(self, button):
        self.manager.article()
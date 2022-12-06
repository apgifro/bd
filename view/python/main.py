from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.tab import MDTabsBase

from controller.corrector import Corrector


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MainScreen(Screen):

    def __init__(self, **kw):
        self.data = {
            'Revisor': ["account", "on_press", self.corrector_press],
            'Artigo': ["book-open-page-variant-outline", "on_press", self.article_press]
        }
        Builder.load_file("view/src/main.kv")
        super().__init__(**kw)
        self.corrector = Corrector()

    def on_enter(self):
        ids = self.manager.get_screen("main").ids
        self.list_corrector = ids.revisores.ids.list
        self.list_article = ids.artigos.ids.list
        self.update_corrector()

    def update_corrector(self):
        select = self.corrector.select()
        self.list_corrector.clear_widgets()
        items = []

        if len(select):
            for selection in select:
                name = selection["nome"]
                item = OneLineListItem(text=name)
                items.append(item)
        else:
            empty = "Clique no + para adicionar um revisor"
            item = OneLineListItem(text=empty)
            items.append(item)

        for item in items:
            self.list_corrector.add_widget(item)

    def corrector_press(self, button):
        self.manager.corrector()

    def article_press(self, button):
        self.manager.article()
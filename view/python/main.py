from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.tab import MDTabsBase

from controller.corrector import Corrector
from controller.author import Author


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MainScreen(Screen):

    def __init__(self, **kw):
        self.data = {
            'Revisor': ["account", "on_press", self._corrector_press],
            'Autor': ["book-edit", "on_press", self._author_press]
        }
        Builder.load_file("view/src/main.kv")
        super().__init__(**kw)
        self.corrector = Corrector()
        self.author = Author()

    def on_enter(self):
        ids = self.manager.get_screen("main").ids
        self.list_corrector = ids.revisores.ids.list
        self.list_author = ids.artigos.ids.list
        self._update_corrector()
        self._update_author()

    def _update_corrector(self):
        select = self.corrector.select()
        self.list_corrector.clear_widgets()
        items = []

        if select:
            for selection in select:
                name = selection["nome"]
                description = f"Especialista em {selection['especialidade']} no(a) {selection['instituicao']}."
                item = TwoLineListItem(text=name,
                                       secondary_text=description,
                                       id=str(selection["id"]),
                                       on_release=self._click_corrector)
                items.append(item)
        else:
            empty = "Adicione o primeiro revisor."
            item = OneLineListItem(text=empty)
            items.append(item)

        for item in items:
            self.list_corrector.add_widget(item)

    def _update_author(self):
        select = self.author.select()
        self.list_author.clear_widgets()
        items = []

        if select:
            for selection in select:
                name = selection["nome"]
                description = f"Representante do(a) {selection['instituicao']}."
                item = TwoLineListItem(text=name,
                                       secondary_text=description,
                                       id=str(selection["id"]),
                                       on_release=self._click_author)
                items.append(item)
        else:
            empty = "Adicione o primeiro autor."
            item = OneLineListItem(text=empty)
            items.append(item)

        for item in items:
            self.list_author.add_widget(item)

    def _click_corrector(self, item):
        self.manager.corrector()
        screen = self.manager.get_screen("corrector")
        screen.update = True
        screen.update_id = item.id

    def _click_author(self, item):
        self.manager.author()
        screen = self.manager.get_screen("author")
        screen.update = True
        screen.update_id = item.id

    def _corrector_press(self, button):
        self.manager.corrector()

    def _author_press(self, button):
        self.manager.author()

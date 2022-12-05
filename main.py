from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MainScreen(Screen):

    def __init__(self, **kw):
        self.data = {
            'Revisor': ["account", "on_press", self.corrector],
            'Artigo': ["book-open-page-variant-outline", "on_press", self.article]
        }
        Builder.load_file("view/main.kv")
        super().__init__(**kw)

    def on_enter(self):
        print(self.manager.get_screen("main").ids)

    def corrector(self, button):
        self.manager.corrector()

    def article(self, button):
        self.manager.article()


class CorrectorScreen(Screen):

    Builder.load_file("view/corrector.kv")


class ArticleScreen(Screen):

    Builder.load_file("view/article.kv")


class ScreenManagement(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def main(self):
        self.current = "main"

    def article(self):
        self.current = "article"

    def corrector(self):
        self.current = "corrector"

    def back(self):
        self.transition = SlideTransition(direction="right")
        self.main()
        self.transition = SlideTransition(direction="left")


class Evento(MDApp):

    def __init__(self):

        super().__init__()
        self.manager = ScreenManagement()

    def build(self):

        main = MainScreen(name="main")
        author = CorrectorScreen(name="corrector")
        article = ArticleScreen(name="article")

        self.manager.add_widget(main)
        self.manager.add_widget(article)
        self.manager.add_widget(author)
        self.manager.main()

        return self.manager


if __name__ == '__main__':
    Evento().run()
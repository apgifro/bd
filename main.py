from kivymd.app import MDApp

from view.python.manager import ScreenManagement

from view.python.main import MainScreen
from view.python.corrector import CorrectorScreen
from view.python.article import ArticleScreen


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

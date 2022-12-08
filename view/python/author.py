from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton

from controller.author import Author


class AuthorScreen(Screen):
    def __init__(self, **kw):
        Builder.load_file("view/src/author.kv")
        super().__init__(**kw)
        self.author = Author()
        self.update = False
        self.update_id = -1

    def on_enter(self, *args):
        self.ids = self.manager.get_screen("author").ids
        self.ids.delete_box.clear_widgets()

        if self.update:
            self.ids.delete_box.add_widget(MDRaisedButton(
                id="delete_button",
                text="Excluir",
                pos_hint={"x": 0.03},
                md_bg_color="red",
                size_hint=(0.2, 0),
                on_release=self.delete),
            )

            select = self.author.select_id(self.update_id)
            self.select = self.author.select_id(self.update_id)

            if select:
                self.ids.name.text = select["nome"]
                self.ids.domain.text = select["instituicao"]
                self.ids.email.text = select["email"]


    def back(self):
        self.update = False
        self.update_id = -1
        self.ids.name.text = ""
        self.ids.domain.text = ""
        self.ids.email.text = ""
        self.manager.back()

    def save(self):
        try:
            name = self.ids.name.text
            domain = self.ids.domain.text
            email = self.ids.email.text

        except Exception as e:
            print(e)
            toast("Digite corretamente")

        else:
            data = {"nome": name,
                    "instituicao": domain,
                    "email": email}

            if self.update:
                save = self.author.save(id=self.update_id, **data)
                self.update = False
                self.update_id = -1
            else:
                save = self.author.save(**data)

            if save:
                toast("Salvo")
                self.back()
            else:
                toast("Erro")

    def delete(self, button):
        delete = self.author.delete(self.update_id)
        if delete:
            toast("Excluído")
            self.back()
        else:
            toast("Erro")

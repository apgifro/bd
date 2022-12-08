from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton

from controller.corrector import Corrector


class CorrectorScreen(Screen):

    def __init__(self, **kw):
        Builder.load_file("view/src/corrector.kv")
        super().__init__(**kw)
        self.corrector = Corrector()
        self.update = False
        self.update_id = -1

    def on_enter(self, *args):
        self.ids = self.manager.get_screen("corrector").ids
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

            select = self.corrector.select_id(self.update_id)
            self.select = self.corrector.select_id(self.update_id)

            if select:
                self.ids.name.text = select["nome"]
                self.ids.domain.text = select["instituicao"]
                self.ids.street.text = select["rua"]
                self.ids.number.text = str(select["numero"])
                self.ids.district.text = select["bairro"]
                self.ids.city.text = select["cidade"]
                self.ids.uf.text = select["unidade_federativa"]
                self.ids.expertise.text = select["especialidade"]
                self.ids.cellphone.text = str(select["telefone"])
                self.ids.fax.text = str(select["fax"])

    def back(self):
        self.update = False
        self.update_id = -1
        self.manager.back()

    def save(self):
        try:
            name = self.ids.name.text
            domain = self.ids.domain.text
            street = self.ids.street.text
            number = int(self.ids.number.text)
            district = self.ids.district.text
            city = self.ids.city.text
            uf = self.ids.uf.text
            expertise = self.ids.expertise.text
            cellphone = int(self.ids.cellphone.text)
            fax = int(self.ids.fax.text)

            if len(uf) > 2:
                raise
            if len(str(cellphone)) > 9 or len(str(fax)) > 9 or len(str(number)) > 4:
                raise

        except Exception as e:
            print(e)
            toast("Digite corretamente")

        else:
            data = {"nome": name,
                    "instituicao": domain,
                    "rua": street,
                    "numero": number,
                    "bairro": district,
                    "cidade": city,
                    "unidade_federativa": uf,
                    "nome_especialidade": expertise,
                    "telefone": cellphone,
                    "fax": fax}

            if self.update:
                save = self.corrector.save(id=self.update_id, **data)
            else:
                save = self.corrector.save(**data)

            if save:
                toast("Salvo")
                self.back()
            else:
                toast("Erro")

    def delete(self, button):
        delete = self.corrector.delete(self.update_id)
        if delete:
            toast("Excluído")
            self.back()
        else:
            toast("Erro")

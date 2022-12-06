from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast

from controller.corrector import Corrector


class CorrectorScreen(Screen):

    def __init__(self, **kw):
        Builder.load_file("view/src/corrector.kv")
        super().__init__(**kw)
        self.corrector = Corrector()

    def save(self):
        ids = self.manager.get_screen("corrector").ids

        name = ids.name.text
        domain = ids.domain.text
        street = ids.street.text
        number = int(ids.number.text)
        district = ids.district.text
        city = ids.city.text
        uf = ids.uf.text

        save = self.corrector.save(nome=name,
                                   instituicao=domain,
                                   rua=street,
                                   numero=number,
                                   bairro=district,
                                   cidade=city,
                                   unidade_federativa=uf)

        if save:
            toast("Salvo")
        else:
            toast("Erro")

        self.manager.back()

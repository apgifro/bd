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

        try:
            name = ids.name.text
            domain = ids.domain.text
            street = ids.street.text
            number = int(ids.number.text)
            district = ids.district.text
            city = ids.city.text
            uf = ids.uf.text
            expertise = ids.expertise.text
            cellphone = int(ids.cellphone.text)
            fax = int(ids.fax.text)

            if len(uf) > 2:
                raise
            if len(str(cellphone)) > 9 or \
                    len(str(fax)) > 9 or \
                    len(str(street)) > 4:
                raise

        except Exception as e:
            print(e)
            toast("Digite corretamente")

        else:
            save = self.corrector.save(nome=name,
                                       instituicao=domain,
                                       rua=street,
                                       numero=number,
                                       bairro=district,
                                       cidade=city,
                                       unidade_federativa=uf,
                                       especialidade=expertise,
                                       telefone=cellphone,
                                       fax=fax)

            if save:
                toast("Salvo")
            else:
                toast("Erro")

            self.manager.back()

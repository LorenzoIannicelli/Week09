import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        if self._mese is None :
            self._view.create_alert("Seleziona un mese")
        else :
            umidita_media = self._model.get_umidita_media_mese(self._mese)
            self._view.lst_result.controls.clear()
            for dato in umidita_media:
                self._view.lst_result.controls.append(ft.Text(dato[0], dato[1]))

            self._view.update_page()

    def handle_sequenza(self, e):
        # controllare che il mese non sia None
        if self._mese == None :
            self._view.create_alert("Seleziona un mese")
        else :
            sequenza, costo = self._model.genera_sequenza(self._mese)
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text(f'Il costo della soluzione è {costo}'))
            for fermata in sequenza:
                self._view.lst_result.controls.append(ft.Text(fermata))
            self._view.update_page()



    def read_mese(self, e):
        self._mese = int(e.control.value)
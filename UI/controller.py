import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        self._view.txt_result.controls.clear()

        distanza_min = self._view.txt_in.value

        if not self._check_input(distanza_min):
            return

        dist_min = float(distanza_min)
        self._model.buildGraph(dist_min)
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente!", color="green"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato contiene {self._model.get_num_nodi()} vertici e {self._model.get_num_edges()} archi."))
        self._view.txt_result.controls.append(ft.Text(self._model.get_all_archi()))
        self._view.update_page()

    def _check_input(self, distanza_min: str):

        if distanza_min is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Inserisci un valore!", color="red")
            )
            self._view.update_page()
            return False

        try:
            distanza_min_float = float(distanza_min)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Inserisci un valore numerico!", color="red")
            )
            self._view.update_page()
            return False

        self._view.txt_result.controls.clear()
        return True
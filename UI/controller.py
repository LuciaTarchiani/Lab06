import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None

    def fillddAnno(self):
        # dal modello recuperiamo i vari anni delle vendite
        # viene restituita una lista contentente gli anni come numeri
        anni = self._model.getAnni()

        for a in anni:
            self._view._ddAnno.options.append(
                ft.dropdown.Option(key = a, text = a)
            )

    def fillddBrand(self):
        # dal modello recuperiamo i brand da mostrare nella tendina
        brands = self._model.getBrand()

        for b in brands:
            self._view._ddBrand.options.append(
                ft.dropdown.Option(key = b, text = b)
            )

    def fillddRetailer(self):
        # mi faccio passare dal modello la lista di OGGETTI retailer
        retailers = self._model.getRetailer()
        for r in retailers:
            self._view._ddRetailer.options.append(
                ft.dropdown.Option(
                    key = r.Retailer_code,
                    text = r.__str__(),
                    data = r,
                    on_click = self.read_retailer
                )
            )

    def read_retailer(self,e):
        self._retailer = e.control.data

    def getTopVendite(self,e):
        pass

    def getAnalizzaVendite(self,e):
        pass

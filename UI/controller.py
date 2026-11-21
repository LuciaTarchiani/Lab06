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

    def setRetailer(self,e):
        self._retailer = None

    """
    def getTopVendite(self,e):
        #dobbiamo farci restituire una lista di oggetti VENDITA
        # per effettuare le query dobbiamo recuperare dalla view i valori dei vari dropdowm
        # ANNO
        self._view.txt_result.controls.clear()
        anno = self._view._ddAnno.value
        if anno == "Nessun Filtro":
            anno = None
        brand = self._view._ddBrand.value
        if brand == "Nessun Filtro":
            brand = None
        retailer = self._view._ddRetailer.value
        if retailer == "Nessun Filtro":
            retailer = None

        # abbiamo una lista con tutte le vendite richieste
        vendite = self._model.getVendite(anno,brand,retailer)

        n = 0
        while n < 5:
            self._view.txt_result.controls.append(
                ft.TextField(vendite[n].__str__())
            )
            n += 1

        self._view.update_page()
    """

    def getTopVendite(self,e):
        #il model deve resituirici le top vendite, le operazioni di selezione devo essere fatte nel model.
        self._view.txt_result.controls.clear()
        anno = self._view._ddAnno.value
        if anno == "Nessun Filtro":
            anno = None
        brand = self._view._ddBrand.value
        if brand == "Nessun Filtro":
            brand = None
        retailer = self._view._ddRetailer.value
        if retailer == "Nessun Filtro":
            retailer = None
        topVendite = self._model.topVendite(anno,brand,retailer)

        for v in topVendite:
            self._view.txt_result.controls.append(
                ft.TextField(v.__str__())
            )

        self._view.update_page()


    def getAnalizzaVendite(self,e):
        pass

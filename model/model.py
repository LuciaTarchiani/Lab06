from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMapProdotti = {}
        for p in DAO.getProdotti():
            self._idMapProdotti[p.Product_number] = p

        self._allVendite = DAO.getVendite(self._idMapProdotti)

    def getAnni(self):
        # restituisco una lista contente gli anni come numeri
        return DAO.getAnni()

    def getBrand(self):
        return DAO.getBrand()

    def getRetailer(self):
        #ottengo una lista di oggetti Retailer
        return DAO.getRetailer()
    """
    def getVendite(self, anno,brand, retailer):
        return DAO.getVendite(anno,brand,retailer)
    """

    def topVendite(self, anno,brand, retailer):
        #una volta ricavate tutte le vendite possiamo andare a filtrare le vendite sulla base dei valori inseriti dall'utente
        filtrate = self.filtraVendite(anno,brand,retailer)
        filtrate.sort(key=lambda v: v.ricavo(), reverse=True)
        return filtrate[:5]

    def statistiche(self,anno,brand,retailer):
        filtrate = self.filtraVendite(anno, brand, retailer)
        numVendite = len(filtrate)
        totRicavo = 0
        retailerDifferenti = []
        prodottiDifferenti = []
        for v in filtrate:
            totRicavo += v.ricavo()
            if v.Retailer_code not in retailerDifferenti:
                retailerDifferenti.append(v.Retailer_code)
            if v.Product_number not in prodottiDifferenti:
                prodottiDifferenti.append(v.Product_number)
        numRetailer = len(retailerDifferenti)
        numProdotti = len(prodottiDifferenti)
        return [f"giro di affari : {totRicavo}", f"numero vendite: {numVendite}", f"numero retailers: {numRetailer}" , f"numero prodotti: {numProdotti}"]


    def filtraVendite(self,anno,brand,retailer):
        filtrate = []
        for v in self._allVendite:
            if anno is not None and v.Date.year != int(anno):
                continue
            if brand is not None and v.Product.Product_brand != brand:
                continue
            if retailer is not None and v.Retailer_code != int(retailer):
                continue
            filtrate.append(v)
        return filtrate

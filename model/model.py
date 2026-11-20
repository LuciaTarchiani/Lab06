from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAnni(self):
        # restituisco una lista contente gli anni come numeri
        return DAO.getAnni()

    def getBrand(self):
        return DAO.getBrand()

    def getRetailer(self):
        #ottengo una lista di oggetti Retailer
        return DAO.getRetailer()
from database.DB_connect import DBConnect
from model.Retailer import Retailer
from model.daily_sale import Daily_sale
from model.prodotto import Prodotto


class DAO():

    # il dao non ha il costruttore

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = """
                SELECT DISTINCT YEAR(Date) as year
                FROM go_daily_sales 
                Order by year
                """
        cursor.execute(query)

        anni = []
        for a in cursor:
            anni.append(a["year"])

        cursor.close()
        cnx.close()
        return anni

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = ("""
                SELECT DISTINCT product_brand
                FROM go_products 
                ORDER BY Product_brand 
                """)
        cursor.execute(query)

        brands= []
        for b in cursor:
            brands.append(b["product_brand"])

        cursor.close()
        cnx.close()
        return brands

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = """SELECT * 
                FROM go_retailers """
        cursor.execute(query)

        retailers= []

        for r in cursor:
            retailers.append(Retailer(**r))

        cursor.close()
        cnx.close()
        return retailers

    """
    @staticmethod
    def getVendite(anno,brand,retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = 
                SELECT gds.Retailer_code , gds.Product_number , gds.Order_method_code ,gds.`Date` , gds.Quantity ,gds.Unit_price ,gds.Unit_sale_price , gds.Unit_sale_price *gds.Quantity as Ricavo
                FROM go_daily_sales gds , go_products gp 
                WHERE gds.Product_number  = gp.Product_number 
                and YEAR(gds.Date) = COALESCE(%s, YEAR(gds.Date)) 
                and gp.Product_brand = COALESCE(%s, gp.Product_brand)
                and gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                Order by Ricavo DESC
                 
        cursor.execute(query, (anno,brand,retailer))

        vendite = []
        for row in cursor:
            vendite.append(Daily_sale(**row))

        cursor.close()
        cnx.close()
        return vendite
        """

    @staticmethod
    def getProdotti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = "Select * from go_products"
        cursor.execute(query)

        prodotti = []
        for row in cursor:
            prodotti.append(Prodotto(**row))
        cursor.close()
        cnx.close()
        return prodotti

    @staticmethod
    def getVendite(idMapProdotti):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = "Select * from go_daily_sales"
        cursor.execute(query)

        Allvendite = []
        for row in cursor:
            prodotto = idMapProdotti[row["Product_number"]]
            Allvendite.append(Daily_sale(**row, Product= prodotto))

        cursor.close()
        cnx.close()
        return Allvendite





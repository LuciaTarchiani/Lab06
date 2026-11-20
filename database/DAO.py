from database.DB_connect import DBConnect
from model.Retailer import Retailer


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

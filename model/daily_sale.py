import datetime
import decimal
from dataclasses import dataclass

from model.prodotto import Prodotto

"""
@dataclass
class Daily_sale:
    Retailer_code : int
    Product_number: int
    Order_method_code: int
    Date : datetime.date
    Quantity: int
    Unit_price : decimal.Decimal
    Unit_sale_price : decimal.Decimal
    Ricavo : decimal.Decimal

    def __str__(self):
        return (f"Data: {self.Date} - Ricavo {self.Ricavo} - Retailer: {self.Retailer_code} - Product :{self.Product_number }")
"""

@dataclass
class Daily_sale:
    Retailer_code : int
    Product_number: int
    Order_method_code: int
    Date : datetime.date
    Quantity: int
    Unit_price : decimal.Decimal
    Unit_sale_price : decimal.Decimal
    Product: Prodotto

    def __str__(self):
        return (f"{self.Date} - Ricavo {self.Unit_sale_price * self.Quantity} - Product :{self.Product.Product_number}")

    def ricavo(self):
        return self.Unit_sale_price * self.Quantity

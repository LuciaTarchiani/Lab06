import decimal
from dataclasses import dataclass

@dataclass
class Prodotto:
    Product_number: int
    Product_line: str
    Product_type: str
    Product: str
    Product_brand: str
    Product_color: str
    Unit_cost: decimal.Decimal
    Unit_price: decimal.Decimal

    def __eq__(self, other):
        return self.Product_number == other.Product_number

    def __hash__(self):
        return hash(self.Product_number)

    def __str__(self):
        return (f"{self.Product} - {self.Product_brand}")

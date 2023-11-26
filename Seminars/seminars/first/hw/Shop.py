from typing import List
from Product import Product


class Shop:
    def __init__(self):
        self.products: List[Product] = []

    # Getters and setters
    def get_products(self):
        return self.products

    def set_products(self, products):
        self.products = products

    # Cортирует список продуктов по стоимости
    def sort_products_by_price(self):
        return sorted(self.products, key=lambda x: x.get_cost())

    # Возвращает самый дорогой продукт
    def get_most_expensive_product(self):
        return max(self.products, key=lambda x: x.get_cost()) if self.products else None

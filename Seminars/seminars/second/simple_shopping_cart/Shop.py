from typing import List
from Seminars.seminars.second.simple_shopping_cart.Product import Product


class Shop:
    def __init__(self, products_shop: List[Product]):
        # Список продуктов в магазине
        self.products_shop = products_shop

    # Метод для получения текущего списка продуктов
    def get_products_shop(self) -> List[Product]:
        return self.products_shop

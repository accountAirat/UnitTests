from typing import List
from Product import Product
from Shop import Shop
from TextUserInterface import TextUserInterface


def get_store_items() -> List[Product]:
    products = []

    # Три массива Названия, Цены, Кол-во
    product_names = ["bacon", "beef", "ham", "salmon", "carrot", "potato", "onion",
                     "apple", "melon", "rice", "eggs", "yogurt"]
    product_prices = [170.00, 250.00, 200.00, 150.00, 15.00, 30.00, 20.00, 59.00, 88.00, 100.00, 80.00, 55.00]
    stock = [10, 10, 10, 10, 10, 10, 10, 70, 13, 30, 40, 60]

    # Последовательно наполняем список продуктами
    for i in range(len(product_names)):
        products.append(Product(i + 1, product_names[i], product_prices[i], stock[i]))

    return products


if __name__ == "__main__":
    shop = Shop(get_store_items())
    TextUserInterface(shop)

from typing import List
from Seminars.seminars.second.simple_shopping_cart.Product import Product


class Cart:
    def __init__(self, shop):
        # Корзина с продуктами
        self.cart_items: List[Product] = []
        # При создании корзины нужно передать магазин
        self.shop = shop
        self.total_price = 0.00

    # Метод для добавления продукта в корзину по его id
    def add_product_to_cart_by_id(self, product_id: int) -> None:
        product = self.get_product_by_product_id(product_id)
        self.add_to_cart(product)
        self.recalculate()

    def recalculate(self) -> None:
        # Метод пересчитывает сумму покупки
        self.total_price = sum(p.price * p.quantity for p in self.cart_items)

    # Чтобы положить продукт в корзину, его нужно сначала найти в магазине
    def get_product_by_product_id(self, product_id: int) -> Product:
        product = Product()
        products = self.shop.get_products_shop()

        for prod in products:
            if prod.id == product_id:
                product = prod
                break

        if product_id > len(products) or product_id < 0:
            raise ValueError("Не найден продукт с id: " + str(product_id))

        return product

    def add_to_cart(self, product: Product) -> None:
        product_in_cart = Product(product.id, product.name, product.price, 0)
        product_in_shop = self.shop.get_products_shop()[product.id - 1]

        if product_in_shop.quantity == 0:
            print("Этого товара нет в наличии")
            return

        # Изменяем кол-во в корзине +1
        if self.has_contain_product(product_in_cart):
            self.get_contain_product(product_in_cart).quantity += 1
        else:
            product_in_cart.quantity = 1
            self.cart_items.append(product_in_cart)

        self.recalculate()
        # Изменяем кол-во в магазине -1
        product_in_shop.quantity -= 1

    def has_contain_product(self, product: Product) -> bool:
        return any(cart_item.id == product.id for cart_item in self.cart_items)

    def has_contain_product_id(self, product_id: int) -> bool:
        return any(cart_item.id == product_id for cart_item in self.cart_items)

    # Поиск продукта в корзине, если он был уже добавлен ранее
    def get_contain_product(self, product: Product) -> Product:
        for cart_item in self.cart_items:
            if cart_item.id == product.id:
                return cart_item
        return None

    def remove_product_by_id(self, product_id: int) -> None:
        if not self.has_contain_product_id(product_id):
            raise ValueError("В корзине не найден продукт с id: " + str(product_id))

        # Изменяем кол-во в корзине -1
        prod = self.get_product_by_product_id(product_id)
        if self.has_contain_product(prod) and self.get_contain_product(prod).quantity > 1:
            self.get_contain_product(prod).quantity -= 1
        elif self.has_contain_product(prod) and self.get_contain_product(prod).quantity == 1:
            self.cart_items.remove(self.get_contain_product(prod))

        # Небольшая задержка для имитации обработки
        import time
        time.sleep(0.07)

        self.recalculate()

        # Изменяем кол-во в магазине +1
        product_in_shop = self.shop.get_products_shop()[product_id - 1]
        product_in_shop.quantity += 1

    def print_cart_items(self) -> None:
        format_str = "%-3s| %-20s| %-9s| %-3s"
        print("Сейчас у вас в корзине:")
        print(format_str % ("ID", "Название", "Цена, р.", "Кол-во в корзине, шт."))
        for prod in self.cart_items:
            print(format_str % (prod.id, prod.name, prod.price, prod.quantity))
        print("Общая стоимость корзины: " + str(self.total_price) + " р.\n")

    def get_total_price(self) -> float:
        return self.total_price

    def set_total_price(self, total_price: float) -> None:
        self.total_price = total_price

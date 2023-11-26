from typing import List
from Cart import Cart


class TextUserInterface:
    def __init__(self, shop):
        self.shop = shop
        self.cart = Cart(shop)
        self.user_choice = None
        self.menu()

    def start_screen(self):
        print("Выберите одно из действий:")
        print("1. Показать список доступных продуктов")
        print("2. Перейти в корзину")
        print("0. Выход")

    def store_products_menu(self):
        print("Выберите одно из действий:")
        print("1. Добавить в корзину")
        print("2. Удалить из корзины")
        print("0. Выход")

    def menu(self):
        while self.user_choice != 0:
            self.start_screen()
            self.get_user_input()

            if self.user_choice == 1:
                self.display_store_products()
                self.store_products_menu()
                self.get_user_input()
                self.inner_choice()
            elif self.user_choice == 2:
                self.show_cart()
            elif self.user_choice == 0:
                exit()
            else:
                pass

    def inner_choice(self):
        if self.user_choice == 1:
            self.add_product_to_cart()
            self.show_cart()
        elif self.user_choice == 2:
            self.remove_product_from_cart()
            self.show_cart()
        else:
            pass

    def get_user_input(self):
        try:
            self.user_choice = int(input())
            return self.user_choice
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    def display_store_products(self):
        products = self.shop.get_products_shop()
        format_str = "%-3s| %-20s| %-9s| %-3s"
        print(format_str % ("ID", "Название", "Цена, р.", "Кол-во в магазине, шт."))
        for prod in products:
            print(format_str % (prod.get_id(), prod.get_name(), prod.get_price(), prod.get_quantity()))
        print()

    def add_product_to_cart(self):
        print("Введите ID продукта, который хотите добавить в корзину:")
        id = self.get_user_input()
        self.cart.add_product_to_cart_by_id(id)

    def show_cart(self):
        self.cart.print_cart_items()

    def remove_product_from_cart(self):
        print("Введите ID продукта, который хотите удалить:")
        id = self.get_user_input()
        self.cart.remove_product_by_id(id)

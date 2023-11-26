"""
     1. Проверить, что магазин хранит верный список продуктов (количество продуктов, состав корзины)
     2. Проверить, что магазин возвращает верный самый дорого продукт getMostExpensiveProduct
     3. Проверить, что магазин возвращает верный отсортированный по цене список продуктов
"""
import unittest
from Seminars.seminars.first.hw.Shop import Shop
from Seminars.seminars.first.hw.Product import Product


class ShopTest(unittest.TestCase):
    def setUp(self):
        self.test_list = list()
        for i in range(1, 10+1):
            self.test_list.append(Product())
            self.test_list[-1].set_cost(i * 330)
            self.test_list[-1].set_title(f"Product {i}")

        self.shop = Shop()
        self.shop.set_products(self.test_list)

    def test_get_products(self):
        self.assertEqual(len(self.shop.get_products()), 10)

    def test_get_most_expensive_product(self):
        most_expensive_product = self.shop.get_most_expensive_product()
        self.assertEqual(most_expensive_product.get_cost(), 3300)
        self.assertEqual(most_expensive_product.get_title(), "Product 10")

    def test_sort_products_by_price(self):
        sorted_products = self.shop.sort_products_by_price()
        self.assertEqual(sorted_products[0].get_cost(), 330)
        self.assertEqual(sorted_products[-1].get_cost(), 3300)


if __name__ == '__main__':
    unittest.main()

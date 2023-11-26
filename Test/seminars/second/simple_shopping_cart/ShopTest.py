from typing import List
import unittest
from assertpy import assert_that
from parameterized import parameterized

from Seminars.seminars.second.simple_shopping_cart.Product import Product
from Seminars.seminars.second.simple_shopping_cart.Cart import Cart
from Seminars.seminars.second.simple_shopping_cart.Shop import Shop


class ShopTest(unittest.TestCase):

    # Создаем набор продуктов для магазина:
    def get_store_items(self) -> List[Product]:
        # Три массива Названия, Цены, Кол-во
        product_names = ["bacon", "beef", "ham", "salmon", "carrot", "potato", "onion", "apple", "melon", "rice",
                         "eggs", "yogurt"]
        product_price = [170.00, 250.00, 200.00, 150.00, 15.00, 30.00, 20.00, 59.00, 88.00, 100.00, 80.00, 55.00]
        stock = [10, 10, 10, 10, 10, 10, 10, 70, 13, 30, 40, 60]

        # Последовательно наполняем список продуктами
        products = [Product(i + 1, product_names[i], product_price[i], stock[i]) for i in range(len(product_names))]
        return products

    # private ByteArrayOutputStream output = new ByteArrayOutputStream();
    #
    # // private Shop shop;
    # // private Cart cart;
    # //  @BeforeEach
    # //  void setup() {
    # //      shop = new Shop(getStoreItems());
    # //      cart = new Cart(shop);
    # //  }

    # ID | Название  | Цена, р. | Кол-во в магазине, шт.
    # 1  | bacon     | 170.0    | 10
    # 2  | beef      | 250.0    | 10
    # 3  | ham       | 200.0    | 10
    # 4  | salmon    | 150.0    | 10
    # 5  | carrot    | 15.0     | 10
    # 6  | potato    | 30.0     | 10
    # 7  | onion     | 20.0     | 10
    # 8  | apple     | 59.0     | 70
    # 9  | melon     | 88.0     | 13
    # 10 | rice      | 100.0    | 30
    # 11 | eggs      | 80.0     | 40
    # 12 | yogurt    | 55.0     | 60

    # * 2.1. Разработайте модульный тест для проверки, что общая стоимость
    # * корзины с разными товарами корректно рассчитывается
    # * <br><b>Ожидаемый результат:</b>
    # * Стоимость корзины посчиталась корректно

    def test_price_cart_is_correct_calculated(self):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)
        # Act
        cart.add_product_to_cart_by_id(1)
        cart.add_product_to_cart_by_id(2)
        # Assert
        self.assertEqual(cart.get_total_price(), 170 + 250)

    # * 2.2. Создайте модульный тест для проверки, что общая стоимость
    # * корзины с множественными экземплярами одного и того же продукта корректно рассчитывается.
    # * <br><b>Ожидаемый результат:</b>
    # * Стоимость корзины посчиталась корректно

    def test_price_cart_products_same_type_is_correct_calculated(self):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)

        # Act
        cart.add_product_to_cart_by_id(1)
        cart.add_product_to_cart_by_id(2)
        cart.add_product_to_cart_by_id(3)
        cart.add_product_to_cart_by_id(4)
        # Assert
        self.assertEqual(cart.get_total_price(), 770)

    # * 2.3. Напишите модульный тест для проверки, что при удалении
    # * товара из корзины происходит перерасчет общей стоимости корзины.
    # * <br><b>Ожидаемый результат:</b>
    # * Вызывается метод пересчета стоимости корзины, стоимость корзины меняется

    def test_when_changing_cart_cost_recalculation_is_called(self):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)
        # Act
        cart.add_product_to_cart_by_id(1)
        cart.add_product_to_cart_by_id(1)
        cart.add_product_to_cart_by_id(1)
        cart.remove_product_by_id(1)
        # Assert
        self.assertEqual(cart.get_total_price(), 170 + 170)

    # * 2.4. Разработайте модульный тест для проверки, что при добавлении определенного количества товара в корзину,
    # * общее количество этого товара в магазине соответствующим образом уменьшается.
    # * <br><b>Ожидаемый результат:</b>
    # * Количество товара в магазине уменьшается на число продуктов в корзине пользователя

    def test_quantity_products_store_changing(self):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)

        # Act
        cart.add_product_to_cart_by_id(4)
        cart.add_product_to_cart_by_id(4)

        # Assert
        self.assertEqual(shop.get_products_shop()[3].get_quantity(), 8)

    # * 2.5. Создайте модульный тест для проверки, что если пользователь забирает все имеющиеся продукты о
    # * пределенного типа из магазина, эти продукты больше не доступны для заказа.
    # * <br><b>Ожидаемый результат:</b>
    # * Больше такой продукт заказать нельзя, он не появляется на полке

    def test_last_products_disappear_from_store(self):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)

        # Act
        for i in range(11):
            cart.add_product_to_cart_by_id(1)

        # Assert
        self.assertEqual(cart.cart_items[0].get_quantity(), 10)

    #
    # * 2.6. Напишите модульный тест для проверки, что при удалении товара из корзины,
    # * общее количество этого товара в магазине соответствующим образом увеличивается.
    # * <br><b>Ожидаемый результат:</b>
    # * Количество продуктов этого типа на складе увеличивается на число удаленных из корзины продуктов
    def test_deleted_product_is_returned_to_shop(self):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)

        # Act
        cart.add_product_to_cart_by_id(3)
        cart.add_product_to_cart_by_id(3)
        cart.add_product_to_cart_by_id(3)
        cart.remove_product_by_id(3)

        # Assert
        self.assertEqual(shop.get_products_shop()[3 - 1].get_quantity(), 8)

    # # * 2.7. Разработайте параметризованный модульный тест для проверки,
    # # * что при вводе неверного идентификатора товара генерируется исключение RuntimeError.
    # # * <br><b>Ожидаемый результат:</b>
    # # * Исключение типа RuntimeError и сообщение Не найден продукт с id
    # # * *Сделать тест параметризованным
    @parameterized.expand([14, 15, 13, 113])
    def test_incorrect_product_selection_causes_exception(self, id: int):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)
        # Act
        cart.add_product_to_cart_by_id(3)

        # Assert
        with self.assertRaises(IndexError):
            shop.get_products_shop()[id]

    # * 2.8. Создайте модульный тест для проверки, что при попытке удалить из корзины больше товаров,
    # * чем там есть, генерируется исключение RuntimeError.удаляет продукты до того, как их добавить)
    # * <br><b>Ожидаемый результат:</b> Исключение типа NoSuchFieldError и сообщение "В корзине не найден продукт с id"
    def test_incorrectProductRemoveCausesException(self):
        # Arrange
        shop = Shop(self.get_store_items())
        cart = Cart(shop)

        # Act
        cart.add_product_to_cart_by_id(3)
        cart.remove_product_by_id(3)

        # Assert
        with self.assertRaises(ValueError):
            cart.remove_product_by_id(3)

    # * 2.9. Нужно восстановить тест
    def test(self):
        shop = Shop(self.get_store_items())
        cart = Cart(shop)

        cart.add_product_to_cart_by_id(2)  # 250
        cart.add_product_to_cart_by_id(2)  # 250

        self.assertEquals(cart.get_total_price(), 500)

    # * 2.10. Нужно оптимизировать тестовый метод, согласно следующим условиям:
    # * <br> 1. Отображаемое имя - "Advanced test for calculating TotalPrice"
    # * <br> 2. Тест повторяется 10 раз
    # * <br> 3. Установлен таймаут на выполнение теста 70 Миллисекунд (unit = TimeUnit.MILLISECONDS)
    # * <br> 4. После проверки работоспособности теста, его нужно выключить

# Не нашёл нужные декораторы

    # def test_sum(self):
    #     # Arrange
    #     shop = Shop(self.get_store_items())
    #     cart = Cart(shop)



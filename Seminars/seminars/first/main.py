from datetime import datetime
from assertpy import assert_that

from Seminars.seminars.first.model.Hero import Hero


def main():
    assert_condition_a()
    assert_condition_b()
    print(sum_numbers(2_147_483_647, 2))
    happy_new_year()
    expected_value()
    checking_shopping_cart()

    colors = ["aqua", "orange", "yellow", "blue", "green", "violet", "gold"]
    testing_collections_assert(colors)

    hero_inventory = ["Bow", "Axe", "Gold"]
    emmett = Hero("Emmett", 50, "sword", hero_inventory, True)
    checking_hero(emmett)




# 1) Нужно найти и исправить ошибку в условиях assert
def assert_condition_a() -> None:
    weekends = ["Суббота", "Воскресенье"]
    assert len(weekends) == 2
    print(f"В неделе {len(weekends)} дня выходных")


# 2) Нужно найти и исправить ошибку в условиях assert
def assert_condition_b() -> None:
    x = -1
    assert x <= 0


"""
 3) Нужно, используя данную функцию, попробовать сложить два следующих числа
 2_147_483_647 и 1, написать assert если нужно
 (https://habr.com/ru/company/pvs-studio/blog/306748/)
"""


def sum_numbers(a, b) -> int:
    return a + b


"""
4) Нужно найти и исправить ошибку в условиях assert
    windows fail - https://habr.com/ru/company/pvs-studio/blog/698404/
"""


def happy_new_year():
    current_date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    assert current_date_time >= "01/01/2023 00:00:00", "Еще 2022 год :("
    print("С новым годом!")


# 5) Утверждение предупреждает об ошибке, нужно исправить код, чтобы утверждение не выбрасывало ошибку
def checking_shopping_cart():
    product_categories = ["fruits", "vegetables", "bakery", "drinks"]
    products = ["apple", "tomato", "bread", "water"]

    for product in products:
        if product == "apple":
            print("category:", product_categories[0])
        elif product == "tomato":
            print("category:", product_categories[1])
        elif product == "bread":
            print("category:", product_categories[2])
        elif product == "water":
            print("category:", product_categories[3])
        else:
            assert False, f"Unknown category for the product {product}"


# 6) Найдите ошибку
def expected_value():
    assert_that(5).is_equal_to(sum_numbers(2, 3))


# Нужно передать в метод массив, который соответствует условиям в утверждении
def testing_collections_assert(colors):
    assert_that(colors) \
        .is_not_empty() \
        .does_not_contain_duplicates() \
        .contains("orange", "green", "violet") \
        .ends_with("gold") \
        .starts_with("aqua") \
        .contains_sequence("yellow", "blue") \
        .does_not_contain("red", "black")
    # .has_size(2) \


"""
     * 8) Удовлетворить всем условиям: <p>
     * 1. Проверить, что герой создался с именем Emmett<p>
     * 2. Проверить, что значение прочности брони героя равно 50<p>
     * 3. Проверить, что у героя оружие типа sword<p>
     * 4. Проверить содержимое инвентаря героя (размер 3, содержимое "Bow", "Axe", "Gold", порядок не важен)<p>
     * 5. Проверить, что герой это человек (свойство isHuman)<p>
"""


def checking_hero(hero):
    assert hero.name == "Emmett"
    assert hero.armor_strength == 50
    assert hero.weapon_type == "sword"
    assert len(hero.inventory) == 3
    assert set(hero.inventory) == set(["Bow", "Axe", "Gold"])
    assert hero.is_human


if __name__ == "__main__":
    main()

# pip install Assertpy

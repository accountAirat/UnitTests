from typing import Optional

class Product:
    def __init__(self, id: Optional[int] = None, name: Optional[str] = None,
                 price: Optional[float] = None, quantity: Optional[int] = None):
        # У продукта есть порядковый номер
        self.id = id
        # У продукта есть порядковое имя
        self.name = name
        # У продукта есть цена
        self.price = price
        # У продукта есть переменная, которая хранит его количество в магазине
        self.quantity = quantity

    # Геттеры для всех полей (методы для получения значений полей):
    def get_id(self) -> Optional[int]:
        return self.id

    def get_name(self) -> Optional[str]:
        return self.name

    def get_price(self) -> Optional[float]:
        return self.price

    def get_quantity(self) -> Optional[int]:
        return self.quantity

    # Сеттеры для всех полей (методы для установки значений полей):
    def set_id(self, id: Optional[int]) -> None:
        self.id = id

    def set_name(self, name: Optional[str]) -> None:
        self.name = name

    def set_price(self, price: Optional[float]) -> None:
        self.price = price

    def set_quantity(self, quantity: Optional[int]) -> None:
        self.quantity = quantity

    # Служебные методы для сравнения продуктов между собой
    def __hash__(self) -> int:
        return hash((self.id, self.name, self.price, self.quantity))

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, Product):
            return False
        return (self.id, self.name, self.price, self.quantity) == (
            other.id, other.name, other.price, other.quantity)

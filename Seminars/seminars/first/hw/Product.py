class Product:
    def __init__(self):
        self.cost = 0  # Стоимость продукта
        self.title = ""  # Название

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year_release = year
        self.num_wheels = 0
        self.speed = 0

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass

    def get_company(self):
        return self.company

    def get_model(self):
        return self.model

    def get_year_release(self):
        return self.year_release

    def get_num_wheels(self):
        return self.num_wheels

    def get_speed(self):
        return self.speed

from Seminars.seminars.second.hw.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, year):
        super().__init__(company, model, year)
        self.num_wheels = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

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

    def __str__(self):
        return f"This car is a {self.year} {self.make} {self.model}"

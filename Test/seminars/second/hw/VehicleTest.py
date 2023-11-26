import unittest

from Seminars.seminars.second.hw.Car import Car
from Seminars.seminars.second.hw.Vehicle import Vehicle

from Seminars.seminars.second.hw.Motorcycle import Motorcycle

"""
Проект Vehicle. Написать следующие тесты с использованием JUnit5:


В этом проекте, вы будете работать с проектом ""Vehicle"", который представляет собой иерархию классов, включающую абстрактный базовый класс ""Vehicle"" и два его подкласса ""Car"" и ""Motorcycle"".
Базовый класс ""Vehicle"" содержит абстрактные методы ""testDrive()"" и ""park()"", а также поля ""company"", ""model"", ""yearRelease"", ""numWheels"" и ""speed"".
Класс ""Car"" расширяет ""Vehicle"" и реализует его абстрактные методы. При создании объекта ""Car"", число колес устанавливается в 4, а скорость в 0. В методе ""testDrive()"" скорость устанавливается на 60, а в методе ""park()"" - обратно в 0.
Класс ""Motorcycle"" также расширяет ""Vehicle"" и реализует его абстрактные методы. При создании объекта ""Motorcycle"", число колес устанавливается в 2, а скорость в 0. В методе ""testDrive()"" скорость устанавливается на 75, а в методе ""park()"" - обратно в 0.
"""


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.car = Car(company='company 1', model='model 1', year=1990)
        self.moto = Motorcycle(company='company 2', model='model 2', year=2000)

    # - Проверить, что экземпляр объекта Car также является
    # экземпляром транспортного средства (используя оператор instanceof).
    def test_car_instanceof_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))

    # - Проверить, что объект Car создается с 4-мя колесами.
    def test_car_num_wheels(self):
        self.assertEquals(self.car.num_wheels, 4)

    # - Проверить, что объект Motorcycle создается с 2-мя колесами.
    def test_motorcycle_num_wheels(self):
        self.assertEquals(self.moto.num_wheels, 2)

    # - Проверить, что объект Car развивает скорость 60
    # в режиме тестового вождения (используя метод testDrive()).
    def test_car_test_drive_speed(self):
        self.car.test_drive()
        self.assertEquals(self.car.speed, 60)

    # - Проверить, что объект Motorcycle развивает скорость 75
    # в режиме тестового вождения (используя метод testDrive()).
    def test_motorcycle_test_drive_speed(self):
        self.moto.test_drive()
        self.assertEquals(self.moto.speed, 75)

    # - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта)
    # машина останавливается (speed = 0).
    def test_car_park_speed(self):
        self.car.test_drive()
        self.car.park()

        self.assertEquals(self.car.speed, 0)

    # - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта)
    # мотоцикл останавливается (speed = 0).
    def test_motorcycle_park_speed(self):
        self.moto.test_drive()
        self.moto.park()
        self.assertEquals(self.moto.speed, 0)

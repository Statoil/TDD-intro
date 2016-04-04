import unittest
from car import Car
from driver import Driver


class TestCar(unittest.TestCase):
    def test_create_car(self):
        car = Car()

    def test_set_model_in_constructor(self):
        car = Car("Toyota")
        self.assertEqual(car.model, "Toyota", "Model is set to Toyota")

    def test_set_model_attribute(self):
        car = Car()
        self.assertEqual(car.model, None, "Car model should default to None")
        car.model = "Nissan"
        self.assertEqual(car.model, "Nissan", "Car model should have been set to Nissan")

    def test_crash_bad_car_is_driver_alive(self):
        car = Car("Flikka Automobile")
        car.set_driver(Driver("Kristian Flikka"))

        car.crash()
        self.assertEqual(car.is_driver_alive(), False, "Car crash in a Flikka Automobile leads to absence of life")

    def test_crash_good_car_is_driver_alive(self):
        car = Car("Volvo")
        car.set_driver(Driver("Kristian Flikka"))

        car.crash()
        self.assertEqual(car.is_driver_alive(), True, "People should live through a crash in a Volvo")


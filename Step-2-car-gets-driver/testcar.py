import unittest
from car import Car


class TestCar(unittest.TestCase):
    def test_create_car(self):
        car = Car()
        self.assertIsNotNone(car, "Car should be created, Yeah!")

    def test_set_model_in_constructor(self):
        car = Car("Toyota")
        self.assertEqual(car.model, "Toyota", "Model is set to Toyota")

    def test_set_model_attribute(self):
        car = Car()
        self.assertEqual(car.model, None, "Car model should default to None")
        car.model = "Nissan"
        self.assertEqual(car.model, "Nissan", "Car model should have been set to Nissan")

    def test_crash_car_is_crashed(self):
        car = Car("Flikka Automobile")
        self.assertFalse(car.has_crashed, "Car should not be crashed from the get go")
        car.crash()
        self.assertTrue(car.has_crashed, "Car crash have crashed, so it should have remembered that.")

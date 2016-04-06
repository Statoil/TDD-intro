import unittest
from car import Car


class TestCar(unittest.TestCase):
    def test_create_car(self):
        car = Car()
        self.assertIsNotNone(car, "Car should be created")

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

    def test_get_driver_name(self):
        car = Car("Volvo")
        self.assertIsNone(car.driver_name, "Driver name should be None when not set")

    def test_set_driver_name(self):
        car = Car("Volvo")
        car.driver_name = "Kristian"
        self.assertEqual(car.driver_name, "Kristian", "Driver name should be set to Kristian")

    def test_car_crash_should_kill(self):
        car = Car("Toyota")
        self.assertTrue(car.driver_is_alive, "A new car has an alive driver")
        car.crash()
        self.assertFalse(car.driver_is_alive, "When the Toyota crashes, driver is killed")

import unittest
from car import Car
from driver import Driver


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota")
        self.car.driver = Driver("Nils")

    def tearDown(self):
        self.car = None

    def test_create_car(self):
        self.assertIsNotNone(self.car, "Car should be created")

    def test_set_model_in_constructor(self):
        self.assertEqual(self.car.model, "Toyota", "Model is set to Toyota")

    def test_set_model_attribute(self):
        self.car.model = "Nissan"
        self.assertEqual(self.car.model, "Nissan", "Car model should have been set to Nissan")

    def test_crash_car_is_crashed(self):
        self.assertFalse(self.car.has_crashed, "Car should not be crashed from the get go")
        self.car.crash()
        self.assertTrue(self.car.has_crashed, "Car crash have crashed, so it should have remembered that.")

    def test_set_driver(self):
        self.car.driver = Driver("Kristian")
        self.assertEqual(self.car.driver_name(), "Kristian", "Name of driver should be Kristian")

    def test_car_crash_should_kill(self):
        self.assertTrue(self.car.driver.is_alive(), "A new car has an alive driver")
        self.car.crash()
        self.assertFalse(self.car.driver.is_alive(), "When the car crashes, driver is killed")

    def test_car_crash_volvo_driver_survives(self):
        self.car.model = "Volvo"
        self.assertTrue(self.car.driver.is_alive(), "A new car has an alive driver")
        self.car.crash()
        self.assertTrue(self.car.driver.is_alive(), "When the Volvo crashes, driver lives")

    def test_car_crash_superman_lives(self):
        self.car.driver = Driver("Superman")
        self.assertTrue(self.car.driver.is_alive(), "A new car has an alive driver")
        self.car.crash()
        self.assertTrue(self.car.driver.is_alive(), "When the car crashes, Superman lives")

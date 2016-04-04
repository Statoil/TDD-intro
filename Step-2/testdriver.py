# Task: Create tests that check a Car object, sets and checks name, age and gender
import unittest
from driver import Driver

class DriverTest(unittest.TestCase):
    def test_create_driver(self):
        driver = Driver()
        self.assertIsNotNone(driver, "Driver should not be None")

    def test_create_with_constructor(self):
        driver = Driver("Nils")
        self.assertEqual(driver.name, "Nils", "Name should be Nils")

    def test_set_name(self):
        driver = Driver()
        driver.name = "Birger"
        self.assertEqual(driver.name, "Birger", "Name should equal Birger")

    def test_get_name_name_not_set(self):
        driver = Driver()
        self.assertEqual(driver.name, None, "Name should be set to None")



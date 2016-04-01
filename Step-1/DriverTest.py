# Task: Create tests that check a Driver object, sets and checks name, age and gender

import unittest

class DriverTest(unittest.TestCase):
    def test_create_driver(self):
        driver = Driver()


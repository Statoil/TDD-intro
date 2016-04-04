
class Car:
    def __init__(self, model=None):
        self.driver = None
        self.model = model

    def crash(self):
        if (self.model != "Volvo"):
            self.driver.kill()

    def set_driver(self, the_driver):
        self.driver = the_driver

    def is_driver_alive(self):
        return self.driver.is_alive()


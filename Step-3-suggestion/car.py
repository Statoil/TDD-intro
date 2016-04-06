
class Car:
    def __init__(self, model=None):
        self.has_crashed = False
        self.model = model
        self.driver = None

    def crash(self):
        self.has_crashed = True
        if self.driver.name is not "Superman" and self.model is not "Volvo":
            self.driver.kill()

    def driver_name(self):
        return self.driver.name


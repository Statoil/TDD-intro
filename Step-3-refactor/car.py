
class Car:
    def __init__(self, model=None):
        self.has_crashed = False
        self.model = model
        self.driver_name = None
        self.driver_is_alive = True

    def crash(self):
        self.has_crashed = True
        self.driver_is_alive = False



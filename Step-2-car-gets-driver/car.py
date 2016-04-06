
class Car:
    def __init__(self, model=None):
        self.has_crashed = False
        self.model = model

    def crash(self):
        self.has_crashed = True



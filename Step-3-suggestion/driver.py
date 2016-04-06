
class Driver:
    def __init__(self, name=None):
        self.name = name
        self._alive = True

    def is_alive(self):
        return self._alive

    def kill(self):
        self._alive = False



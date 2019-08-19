from Engine.Object import StoredObject

class Calculation(StoredObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def run(self, *args):
        raise NotImplementedError()
from Engine.Object import StoredObject

class Data(StoredObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def need_to_be_cached(self):
        return self.check_attribute('need_to_be_cached')
    
    def get_data(self):
        raise NotImplementedError()
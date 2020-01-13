from Engine.Object import StoredObject

class InvalidDataException(Exception):
    """ Exception raised when trying to attach invalid data """
    def __init__(self, message='The data to attach is invalid'):
        super().__init__(self, message)

class Data(StoredObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def get_suffix(self) -> str:
        return '.data'

    def need_to_be_cached(self) -> bool:
        return self.check_attribute('need_to_be_cached')

    def attach(self, data) -> None:
        raise NotImplementedError()
    
    def get_data(self):
        raise NotImplementedError()
from DataModules.Data import Data

class Table(Data):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        
    def has_header(self):
        return self.check_attribute('has_header')

    def get_delimeter(self):
        return self.get_attribute('delimeter', '\t')

    def get_encoding(self):
        return self.get_attribute('encoding', 'utf8')
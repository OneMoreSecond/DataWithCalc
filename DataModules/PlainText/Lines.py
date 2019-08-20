from DataModules.Data import Data

class Lines(Data):
    def __init__(self, data=None, **kwargs):
        super().__init__(self, **kwargs)
        self.data = [] if data is None else data

    def get_suffix(self):
        return '.txt'

    def get_encoding(self):
        return self.get_attribute('encoding', 'utf8')

    def load(self):
        with open(self.get_path(), 'r', encoding=self.get_encoding()) as f:
            self.lines = [line.rstrip('\n') for line in f.readlines()]

    def save(self):
        with open(self.get_path(), 'w', encoding=self.get_encoding()) as f:
            f.writelines([line + '\n' for line in self.lines])

    def get_data(self):
        return self.lines
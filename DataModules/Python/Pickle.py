import pickle

from DataModules.Data import Data

class Pickle(Data):
    def __init__(self, data, **kwargs):
        super().__init__(self, **kwargs)
        self.data = None if data is None else data

    def load(self):
        self.data = pickle.load(self.get_path())

    def save(self):
        pickle.dump(self.data, self.get_path())

    def get_data(self):
        return self.data
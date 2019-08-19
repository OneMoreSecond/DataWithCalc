from Engine.Object import StoredObject
from DataModules.Data import Data
from CalculationModules.Calculation import Calculation

class Package(StoredObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.data = dict()
        self.calculations = dict()
        self.topo_order = []

    def load(self):
        pass

    def save(self):
        pass

    def get_data(self, key):
        pass

    def add_calculation(self, calc_key, calculation, data_key):
        pass
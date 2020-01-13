from typing import Dict, List

from Engine.Object import StoredObject
from DataModules.Data import Data
from CalculationModules.Calculation import Calculation

class Package(StoredObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.data: Dict[str, Data] = dict()
        self.calculations: Dict[str, Calculation] = dict()
        self.topo_order: List[str] = []

    def load(self) -> None:
        pass

    def save(self) -> None:
        pass

    def get_data(self, key) -> Data:
        pass

    def add_calculation(self, key, calculation) -> None:
        pass
    
    def add_calculated_data(self, key, data) -> None:
        pass
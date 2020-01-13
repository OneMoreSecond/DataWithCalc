from typing import Any
import pickle

from DataModules.Data import Data

class Pickle(Data):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.data: Any = None

    def load(self) -> None:
        self.data = pickle.load(self.get_path())

    def save(self) -> None:
        pickle.dump(self.data, self.get_path())

    def attach(self, data: Any) -> None:
        self.data = data

    def get_data(self) -> Any:
        return self.data
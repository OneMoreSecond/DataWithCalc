from typing import List

from Engine.Object import StoredObject
from DataModules.Data import Data

class Calculation(StoredObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def get_suffix(self) -> str:
        return '.calc'

    def run(self, inputs: List[Data], outputs: List[Data]) -> None:
        raise NotImplementedError()
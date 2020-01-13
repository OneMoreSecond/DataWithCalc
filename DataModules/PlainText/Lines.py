from typing import List

from DataModules.Data import Data

class Lines(Data):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.data: List[str] = []

    def get_suffix(self) -> str:
        return '.txt'

    def get_encoding(self) -> str:
        return self.get_attribute('encoding', 'utf8')

    def load(self) -> None:
        with open(self.get_path(), 'r', encoding=self.get_encoding()) as f:
            self.lines = [line.rstrip('\n') for line in f.readlines()]

    def save(self) -> None:
        with open(self.get_path(), 'w', encoding=self.get_encoding()) as f:
            f.writelines([line + '\n' for line in self.lines])

    def attach(self, data: List[str]) -> None:
        self.data = data

    def get_data(self) -> List[str]:
        return self.lines
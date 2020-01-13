from DataModules.Data import Data
from typing import Union
import pandas as pd

class DataFrame(Data):
    def __init__(self, data: Union[pd.DataFrame] =None, **kwargs):
        super().__init__(self, **kwargs)
        self.data: pd.DataFrame = pd.DataFrame()

    def get_suffix(self) -> str:
        return '.' + self.get_store_format()

    def get_store_format(self) -> str:
        return self.get_attribute('store_format', 'hdf')

    def need_to_save_index(self) -> bool:
        return self.check_attribute('write_index')

    def load(self) -> None:
        store_format: str = self.get_store_format()

        if store_format == 'hdf':
            self.data = pd.read_hdf(self.get_path(), 'df')
        elif store_format == 'tsv':
            self.data = pd.read_csv(self.get_path(), sep='\t', index_col=0 if self.need_to_save_index() else False)
        else:
            assert False

    def save(self):
        store_format: str = self.get_store_format()

        if store_format == 'hdf':
            self.data.to_hdf(self.get_path(), 'df')
        elif store_format == 'tsv':
            self.data.to_csv(self.get_path(), sep='\t', index=self.need_to_save_index())
        else:
            assert False

    def attach(self, data: pd.DataFrame) -> None:
        self.data = data

    def get_data(self) -> pd.DataFrame:
        return self.data
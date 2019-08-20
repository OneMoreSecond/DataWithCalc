from DataModules.Data import Data
import pandas as pd

class DataFrame(Data):
    def __init__(self, data=None, **kwargs):
        super().__init__(self, **kwargs)
        self.data = pd.DataFrame() if data is None else data

    def get_suffix(self):
        return '.' + self.get_store_format()

    def get_store_format(self):
        return self.get_attribute('store_format', 'hdf')

    def need_to_save_index(self):
        return self.check_attribute('write_index')

    def load(self):
        store_format = self.get_store_format()

        if store_format == 'hdf':
            self.data = pd.read_hdf(self.get_path(), 'df')
        elif store_format == 'tsv':
            self.data = pd.read_csv(self.get_path(), sep='\t', index_col=0 if self.need_to_save_index() else False)
        else:
            assert False

    def save(self):
        store_format = self.get_store_format()

        if store_format == 'hdf':
            self.data.to_hdf(self.get_path(), 'df')
        elif store_format == 'tsv':
            self.data.to_csv(self.get_path(), sep='\t', index=self.need_to_save_index())
        else:
            assert False

    def get_data(self):
        return self.data
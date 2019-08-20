import os

class AttributedObject:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_name(self):
        return self.get_attribute('name', 'undefined')

    def get_attribute(self, key, default=None):
        return self.attributes.get(key, default)

    def check_attribute(self, key, value=True):
        return self.get_attribute(key) == value


class StoredObject(AttributedObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def get_suffix(self):
        return ''

    def get_path(self):
        directory = self.get_directory()
        path = None if directory is None else os.path.join(directory, self.get_name() + self.get_suffix())
        return path

    def get_directory(self):
        directory = self.get_attribute('directory')
        if directory is not None:
            root_path = self.get_attribute('root_path')
            assert root_path is not None
            directory = os.path.join(root_path, directory)
        return directory

    def load(self, path):
        raise NotImplementedError()

    def save(self, path):
        raise NotImplementedError()
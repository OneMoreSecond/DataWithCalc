import os

class AttributedObject:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_attribute(self, key, default=None):
        return self.attributes.get(key, default)

    def check_attribute(self, key, value=True):
        return self.get_attribute(key) == value


class StoredObject(AttributedObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def get_path(self):
        path = self.get_attribute('path')
        if path is not None:
            root_path = self.get_attribute('root_path')
            assert root_path is not None
            path = os.path.join(root_path, path)
        return path

    def load(self, path):
        raise NotImplementedError()

    def save(self, path):
        raise NotImplementedError()
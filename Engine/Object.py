from typing import Any, Optional
import os

class AttributedObject:
    def __init__(self, **kwargs):
        self.attributes = kwargs

    def get_name(self) -> str:
        return self.get_attribute('name', 'undefined')

    def get_attribute(self, key: str, default: Any = None) -> Any:
        return self.attributes.get(key, default)

    def set_attribute(self, key: str, value: Any) -> None:
        self.attributes[key] = value

    def check_attribute(self, key, value: Any = True) -> bool:
        return self.get_attribute(key) == value


class StoredObject(AttributedObject):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def get_suffix(self) -> str:
        return '.stored'

    def get_path(self) -> Optional[str]:
        directory: str = self.get_directory()
        path: Optional[str] = None if directory is None else os.path.join(directory, self.get_name() + self.get_suffix())
        return path

    def get_directory(self) -> Optional[str]:
        directory: Optional[str] = self.get_attribute('directory')
        if directory is not None:
            root_path: Optional[str]= self.get_attribute('root_path')
            assert root_path is not None
            directory = os.path.join(root_path, directory)
        return directory

    def load(self, path) -> None:
        raise NotImplementedError()

    def save(self, path) -> None:
        raise NotImplementedError()
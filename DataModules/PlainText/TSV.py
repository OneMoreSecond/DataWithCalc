from typing import List, Tuple, Optional

from DataModules.Data import Data, InvalidDataException

Row = List[str]

class TSV(Data):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.header: Optional[Row] = None
        self.contents: List[Row] = []
        self.width = None

    def get_suffix(self) -> str:
        return '.tsv'
        
    @property
    def has_header(self) -> bool:
        return self.check_attribute('has_header')

    @has_header.setter
    def has_header(self, value: bool) -> None:
        self.set_attribute('has_header', value)

    def get_delimeter(self) -> str:
        return self.get_attribute('delimeter', '\t')

    def get_encoding(self) -> str:
        return self.get_attribute('encoding', 'utf8')

    def load(self):
        delimeter: str = self.get_delimeter()
        def parse_line(line) -> str:
            return line.rstrip('\n').split(delimeter)
        
        with open(self.get_path(), 'r', encoding=self.get_encoding()) as f:
            if self.has_header:
                header = parse_line(f.readline())
            contents = [parse_line(line) for line in f.readlines()]
        self.attach((header, contents))

    def save(self):
        delimeter: str = self.get_delimeter()
        def join_line(line) -> str:
            return delimeter.join(line) + '\n'
        
        with open(self.get_path(), 'w', encoding=self.get_encoding()) as f:
            if self.has_header:
                f.write(join_line(self.header))
            
            f.writelines([join_line(line) for line in self.contents])

    def attach(self, data: Tuple[Optional[Row], List[Row]]) -> None:
        header, contents = data
        has_header = header is not None
        if has_header:
            width = len(header)
        elif len(contents) > 0:
            width = len(contents[0])
        else:
            width = None
        
        if width is not None:
            for row in contents:
                if len(row) != width:
                    raise InvalidDataException()
        
        self.header, self.contents = data
        self.width = width
        if has_header:
            self.has_header = True

    def get_data(self) -> Tuple[Optional[Row], List[Row]]:
        return (self.header, self.contents)
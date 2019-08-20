from DataModules.Data import Data

class TSV(Data):
    def __init__(self, data, **kwargs):
        super().__init__(self, **kwargs)
        self.header, self.contents = None, [] if data is None else data

    def get_suffix(self):
        return '.tsv'
        
    def has_header(self):
        return self.check_attribute('has_header')

    def get_delimeter(self):
        return self.get_attribute('delimeter', '\t')

    def get_encoding(self):
        return self.get_attribute('encoding', 'utf8')

    def load(self):
        delimeter = self.get_delimeter()
        def parse_line(line):
            return line.rstrip('\n').split(delimeter)
        
        with open(self.get_path(), 'r', encoding=self.get_encoding()) as f:
            if self.has_header:
                self.header = parse_line(f.readline())
            
            self.contents = [parse_line(line) for line in f.readlines()]

    def save(self):
        delimeter = self.get_delimeter()
        def join_line(line):
            return delimeter.join(line) + '\n'
        
        with open(self.get_path(), 'w', encoding=self.get_encoding()) as f:
            if self.has_header:
                f.write(join_line(self.header))
            
            f.writelines([join_line(line) for line in self.contents])

    def get_data(self):
        return (self.header, self.contents)

class Listcompare:
    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename
        self.list = []
    def compare(self):
        filename = open(f'./{self.directory}/{self.filename}')
        lines = filename.readlines()
        for line in lines:
            if not line.strip():
                continue
            else:
                self.list.append(line)
        return self.list


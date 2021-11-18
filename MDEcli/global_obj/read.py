import csv

class Csv:
    def __init__(self, filename):
        self.filename = filename

    def open(self):
        self.list_ids = []
        with open (self.filename, 'r') as file:
            csv_read = csv.DictReader(file)
            for machineid in csv_read:
                self.list_ids.append(machineid['ï»¿Device ID'])
        return self.list_ids
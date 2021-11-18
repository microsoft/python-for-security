from azure.cli.core import get_default_cli

class Create_rg:
    def __init__(self, location, rg):
        self.location = location
        self.rg = rg

    def create_rg(self):
        try:
            get_default_cli().invoke(['az', 'group', 'create', '--location', f'{self.location}', '--resource-group', f'{self.rg}'])
            return self.rg, self.location
        except Exception as e:
            print(e)
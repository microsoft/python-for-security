from azure.cli.core import get_default_cli

class Nsg:

    def __init__(self, rg, computer, source_prefixes, destination_prefixes, destination_ports):
        self.rg = rg
        self.computer = computer
        self.source_prefixes = source_prefixes
        self.destination_prefixes = destination_prefixes
        self.destination_ports = destination_ports
    
    def create_nsg(self):
        try:
            get_default_cli().invoke(['network', 'nsg', 'create', '--name', f'{self.rg}_{self.computer}_nsg', '--resource-group', self.rg])
        except Exception as e:
            print(e)

    def create_nsg_rule(self):
        try:
            get_default_cli().invoke(['network', 'nsg', 'rule', 'create', '--name', f'{self.rg}_{self.computer}_rule', '--resource-group', self.rg, '--nsg-name', f'{self.rg}_{self.computer}_nsg', '--priority', '400', '--source-address-prefixes', self.source_prefixes, '--destination-address-prefixes', self.destination_prefixes, '--protocol', 'Tcp', '--destination-port-ranges', self.destination_ports])
        except Exception as e:
            print(e)
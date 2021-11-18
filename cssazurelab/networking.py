from azure.cli.core import get_default_cli

class Networking:

    def __init__(self, vnet_address_prefixes, rg, computer, subnet_prefixes):
        self.vnet_address_prefixes = vnet_address_prefixes
        self.rg = rg
        self.computer = computer
        self.subnet_prefixes = subnet_prefixes

    def create_vnet(self):
        try:
            get_default_cli().invoke(['az', 'network', 'vnet', 'create', '--address-prefixes', self.vnet_address_prefixes, '--name', f'{self.rg}_vnet', '--resource-group', self.rg])
        except Exception as e:
            print(e)
    
    def create_subnet(self):
        try:
            get_default_cli().invoke(['az', 'network', 'vnet', 'subnet', 'create', '--name', f'{self.rg}_{self.computer}_subnet', '--vnet-name', f'{self.rg}_vnet', '--resource-group', self.rg, '--address-prefixes', self.subnet_prefixes, '--network-security-group', f'{self.rg}_{self.computer}_nsg'])
        except Exception as e:
            print(e)
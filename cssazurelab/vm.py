from azure.cli.core import get_default_cli

class Vm:
    
    def __init__(self, computer, rg, image, count, disks, nsg, user, password, subnet, vnet):
        self.computer = computer
        self.rg = rg
        self.image = image
        self.count = count
        self.disks = disks
        self.nsg = nsg
        self.user = user
        self.password = password
        self.subnet = subnet
        self.vnet = vnet

    def create_vm(self):
        try:
            get_default_cli().invoke(['az', 'vm', 'create', '-n', self.computer, '-g', self.rg, '--image', self.image, '--count', self.count, '--data-disk-sizes-gb', self.disks, '--nsg', self.nsg, '--admin-username', self.user, '--admin-password', self.password, '--subnet', self.subnet, '--vnet-name', self.vnet])
        except Exception as e:
            print(e)
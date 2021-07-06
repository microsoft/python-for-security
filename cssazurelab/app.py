import time
import login
import rg
import nsg
import networking
import vm
import vm_jumpbox
import password

#Login to Azure CLI
new_login = login.Login
new_login.login()

#Create RG
lab_name_input = input('Lab name (one word): ')
lab_name = lab_name_input.lower()
list_of_locations = ['northeurope', 'westeurope', 'westus2', 'eastus']
print('Please choose one of the following locations: ')
for location in list_of_locations:
    print(location)
location_choice = input('Location: ')
while location_choice not in list_of_locations:
    print('Unavailable location. Please try again')
    location_choice = input('Location: ')
else:
    print(f'Location selected - {location_choice}')
new_rg = rg.Create_rg(location, lab_name)
new_rg.create_rg()

#Inputs for VM's
list_of_images = ['CentOS', 'Debian', 'openSUSE-Leap', 'RHEL', 'SLES', 'UbuntuLTS', 'Win2019Datacenter', 'Win2016Datacenter', 'Win2012R2Datacenter', 'Win2008R2SP1', 'Windows-10']
print('Please choose one of the following images: ')
for image in list_of_images:
    print(image)
image_choice = input('Image: ')
while image_choice not in list_of_images:
    print('Unavailable image. Please try again')
    image_choice = input('Image: ')
else:
    print(f'Image selected - {image_choice}')
number_of_vms = input("Number of VM's to build: ")

#Create NSG's
windows10_nsg = nsg.Nsg(new_rg.rg, 'windowsdesktop', '192.168.4.0/24', '192.168.1.0/24', '3389')
windows10_nsg.create_nsg()
windows10_nsg.create_nsg_rule()
windowsserver_nsg = nsg.Nsg(new_rg.rg, 'windowsserver', '192.168.4.0/24', '192.168.2.0/24', '3389')
windowsserver_nsg.create_nsg()
windowsserver_nsg.create_nsg_rule()
linux_nsg = nsg.Nsg(new_rg.rg, 'linux', '192.168.4.0/24', '192.168.3.0/24', '22')
linux_nsg.create_nsg()
linux_nsg.create_nsg_rule()
jumpbox_nsg = nsg.Nsg(new_rg.rg, 'jumpbox', 'Internet', '192.168.4.0/24', '22')
jumpbox_nsg.create_nsg()
jumpbox_nsg.create_nsg_rule()

#Create Networking
new_vnet = networking.Networking('192.168.0.0/16', new_rg.rg, '', '')
new_vnet.create_vnet()
time.sleep(5)
windowsdesktopsubnet = networking.Networking('', new_rg.rg, 'windowsdesktop', '192.168.1.0/24')
windowsdesktopsubnet.create_subnet()
windowsserversubnet = networking.Networking('', new_rg.rg, 'windowsserver', '192.168.2.0/24')
windowsserversubnet.create_subnet()
linuxsubnet = networking.Networking('', new_rg.rg, 'linux', '192.168.3.0/24')
linuxsubnet.create_subnet()
jumpboxsubnet = networking.Networking('', new_rg.rg, 'jumpbox', '192.168.4.0/24')
jumpboxsubnet.create_subnet()

#Crete Jumpbox
jumpbox_password = password.Password.create_password()

jumpboxvm = vm_jumpbox.Vm(f'{new_rg.rg}jbox', new_rg.rg, 'UbuntuLTS', '450', f'{new_rg.rg}_jumpbox_nsg', f'{new_rg.rg}user', jumpbox_password, f'{new_rg.rg}_jumpbox_subnet', f'{new_rg.rg}_vnet')
jumpboxvm.create_vm()

#Create VMs
vms_password = password.Password.create_password()

if image_choice == 'Windows-10':
    windowsdesktopvm = vm.Vm(f'{new_rg.rg}w10', new_rg.rg, 'MicrosoftWindowsDesktop:Windows-10:20h2-pro-g2:latest', number_of_vms, '250', f'{new_rg.rg}_windowsdesktop_nsg', f'{new_rg.rg}user', vms_password, f'{new_rg.rg}_windowsdesktop_subnet', f'{new_rg.rg}_vnet')
    windowsdesktopvm.create_vm()
    print(f'Credentials for Jumpbox - username: {new_rg.rg}user | password: {jumpbox_password}')
    print(f'Credentials for VM {image_choice} - username: {new_rg.rg}user | password: {vms_password}')
elif image_choice == 'Win2019Datacenter' or 'Win2016Datacenter' or 'Win2012R2Datacenter' or 'Win2008R2SP1':
    windowsservernvm = vm.Vm(f'{new_rg.rg}ws', new_rg.rg, image_choice, number_of_vms, '250', f'{new_rg.rg}_windowsserver_nsg', f'{new_rg.rg}user', vms_password, f'{new_rg.rg}_windowsserver_subnet', f'{new_rg.rg}_vnet')
    windowsservernvm.create_vm()
    print(f'Credentials for Jumpbox - username: {new_rg.rg}user | password: {jumpbox_password}')
    print(f'Credentials for VM {image_choice} - username: {new_rg.rg}user | password: {vms_password}')
elif image_choice == 'CentOS' or 'Debian' or 'openSUSE-Leap' or 'RHEL' or 'SLES' or 'UbuntuLTS':
    linuxvm = vm.Vm(f'{new_rg.rg}lx', new_rg.rg, image_choice, number_of_vms, '250', f'{new_rg.rg}_linux_nsg', f'{new_rg.rg}user', vms_password, f'{new_rg.rg}_linux_subnet', f'{new_rg.rg}_vnet')
    linuxvm.create_vm()
    print(f'Credentials for Jumpbox - username: {new_rg.rg}user | password: {jumpbox_password}')
    print(f'Credentials for VM {image_choice} - username: {new_rg.rg}user | password: {vms_password}')
else:
    print(f'Credentials for Jumpbox - username: {new_rg.rg}user | password: {jumpbox_password}')
    print('No VM created - somethong wrong...')
# MDE CLI
This sample code creates an easy way to interact with Microsoft Defedner for Endpoint through a cli. This can be ran from any OS as long it's running python 3.6 or above

# Requirements and Instalation
MDE CLI  can be ran from any OS as long it's running python 3.6 or above. You'll be required to use pip

## Instalation
pip install -r requiremnts.txt

# Usage
python app.py -h --> for help menu
python app.py <choice> -h --> for sub options menu

## Example
 ### python app.py -h
  
  usage: app.py [-h] {actions} ...

MDEcli = A tool manage MDE through CLI

optional arguments:
  -h, --help  show this help message and exit

Available options:
  {actions}   Choose one of the main options. MDEcli -<option> -h for more details for each main option.
    actions   MachineAction resource type

Original project created by Bruno Rodrigues - rodrigues.bruno@microsoft.com
  
  ### python app.py actions -h
  
  usage: app.py actions [-h] [-offboard] [-quick]

optional arguments:
  -h, --help  show this help message and exit
  -offboard   Offboard device from Defender for Endpoint.
  -quick      Initiate Microsoft Defender Antivirus quick scan on a device.
  
  ### python app.py actions -offboard
  This command will allow you to offboard multiple machines at a ytime by using the Device List exported from MDE portal.
 
# Code Distribution
MAKE SURE YOU ALWAYS SEND LICENSE.TXT WITH THE SAMPLE CODE. This mandatory by Microsfot Policy. 
More details - https://internal.evergreen.microsoft.com/en-us/topic/ef3296ef-1480-ae0f-1741-7b838d32fd36 (internal use only)

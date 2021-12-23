# MDE CLI
This sample code creates an easy way to interact with Microsoft Defedner for Endpoint through a cli. This can be ran from any OS as long it's running python 3.6 or above

# Requirements and Instalation
MDE CLI  can be ran from any OS as long it's running python 3.6 or above. You'll be required to use pip

## Instalation
pip install -r requirements.txt

# Usage
Usage is pretyy much straight forward and you can always use the help menu - python app.py "option" -"sub option"

python app.py alerts -list
python app.py actions -offboard

## Examples

### Help menu for Options - python app.py -h
  
usage: app.py [-h] {alerts,investigations,indicators,machines,actions,recommendations,software,vulnerabilities} ...

MDEcli = A tool manage MDE through CLI

optional arguments:
  -h, --help            show this help message and exit

Available options:
  {alerts,investigations,indicators,machines,actions,recommendations,software,vulnerabilities}
                        Choose one of the main options. MDEcli -<option> -h for more details for each main option.
    alerts              Alert resource type
    investigations      Investigation resource type
    indicators          Indicator resource type
    machines            Machine resource type
    actions             Machine Action resource type
    recommendations     Recommendation resource type
    software            Software resource type
    vulnerabilities     vulnerability resource type

Original project created by Bruno Rodrigues - rodrigues.bruno@microsoft.com
  
### Help menu for Sub Options - python app.py option -h

usage: app.py alerts [-h] [-list]

optional arguments:
  -h, --help  show this help message and exit
  -list       Retrieves a collection of Alerts.
PS C:\Users\brro\OneDrive - Microsoft\Documents\VSCode Python\python-for-security\MDEcli> python.exe .\app.py actions -h
usage: app.py actions [-h] [-offboard] [-quick] [-full]

optional arguments:
  -h, --help  show this help message and exit
  -offboard   Offboard device from Defender for Endpoint.
  -quick      Initiate Microsoft Defender Antivirus quick scan on a device.
  -full       Initiate Microsoft Defender Antivirus full scan on a device.
 
# Code Distribution
MAKE SURE YOU ALWAYS SEND LICENSE.TXT WITH THE SAMPLE CODE. This mandatory by Microsfot Policy. 
More details - https://internal.evergreen.microsoft.com/en-us/topic/ef3296ef-1480-ae0f-1741-7b838d32fd36 (internal use only)

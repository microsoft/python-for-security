# MDE2TEAMS #
Simple Python connector for Microsoft Defender Endpoint (MDE) events and Teams Channel.

# About
The MDE2TEAMS will allow Customers to have all new events (alerts, vulnerabilities, Inventory, etc.) posted to one or more Teams Channel automatically, allowing for a much faster response using all capabilities of Microsoft Teams. This connector uses MDE API.

# Installation
REQUIRED: python3
pipenv install -r requirements.txt

If you decide to manually deploy, you'll need to install the follwing python3 libraries:
- getpass4
- argparse
- pymsteams

# Prerequistes
When you run the app, you'll be required to provide the following info:
- Tenant ID
- App ID
- App Secret
- Webhook

Tenant ID, App Id and App Secret you'll need to create a Application Registration in Azure - https://docs.microsoft.com/en-us/skype-sdk/trusted-application-api/docs/registrationinazureactivedirectory. Make sure you allow the proper permissions for WindowsDefenderATP and Microsoft Threat Protection

You'll also need to create webhooks for each Teams Channel where you want to post new events. App Secret and Webhooks will not displat«y back to the user for security reasons

# Help
This application as a help menu for all the options:
python app.py -h

Help Output:
usage: app.py [-h] {alerts,investigations,indicators,machines,machineactions,recommendations,Software,vulnerabilities}

MDE4Teams = A tool to track MDE events in Teams

positional arguments:
  {alerts,investigations,indicators,machines,machineactions,recommendations,Software,vulnerabilities}
                        Select which notifications to List in Teams

optional arguments:
  -h, --help            show this help message and exit

Original project created by Bruno Rodrigues - rodrigues.bruno@microsoft.com

# Usage & Examples
To Run the app (every argument will require to be run separate):
- python app.py alerts
- python app.py vulnerabilities

# To-Do

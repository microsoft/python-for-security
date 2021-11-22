import getpass
import argparse
import time
import sys

from pandas.core.indexes.base import Index
from mde_api_obj import gettoken, offboard
from global_obj import read

#menu argparser
parser = argparse.ArgumentParser(prog='app.py', description='MDEcli = A tool manage MDE through CLI', epilog='Original project created by Bruno Rodrigues - rodrigues.bruno@microsoft.com')
subparsers = parser.add_subparsers(dest='Commands', title='Available options', help='Choose one of the main options. MDEcli -<option> -h for more details for each main option.')
subparsers.required=True

#Machines Actions menu
machineactionsparser = subparsers.add_parser('actions', help='MachineAction resource type')
machineactionsparser.add_argument('-offboard', help='Offboard device from Defender for Endpoint.', action='store_true')
machineactionsparser.add_argument('-quick', help='Initiate Microsoft Defender Antivirus quick scan on a device.', action='store_true')

args = parser.parse_args()

#Login token
try:
    tenantid = input('Please enter your Tenant ID: ')
    appid = input('Please enter your Application ID: ')
    secret = getpass.getpass('Please enter your Application Secret:')
    new_token = gettoken.GetToken(tenantid, appid, secret)
    new_token.gettoken()
    token = new_token.aadToken

#Actions
    if args.Commands == 'actions':
        if args.offboard:
            filename = input('Please enter the CSV filename (export from MDE/Devices): ')
            comment = input('Comment (mandatory): ')
            new_csv = read.Csv(filename)
            new_csv.open()
            for ids in new_csv.list_ids:
                new_offboard_action = offboard.Offboard(token, ids, comment)
                new_offboard_action.offboard()
        elif args.quick:
            print("Let's quick scan")
        else:
            parser.print_help()
    else:
        parser.print_help()
except Exception as e:
    print(e)
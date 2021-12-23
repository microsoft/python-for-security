import getpass
import argparse
import sys
from mde_api_obj import actions, gettoken, list
from global_obj import read

#menu argparser
parser = argparse.ArgumentParser(prog='app.py', description='MDEcli = A tool manage MDE through CLI', epilog='Original project created by Bruno Rodrigues - rodrigues.bruno@microsoft.com')
subparsers = parser.add_subparsers(dest='Commands', title='Available options', help='Choose one of the main options. MDEcli -<option> -h for more details for each main option.')
subparsers.required=True

#Alerts menu
alertsparser = subparsers.add_parser('alerts', help='Alert resource type')
alertsparser.add_argument('-list', help='Retrieves a collection of Alerts.', action='store_true')

#Automated Investigations menu
investigationparser = subparsers.add_parser('investigations', help='Investigation resource type')
investigationparser.add_argument('-list', help='Retrieves a collection of Investigations.', action='store_true')

#Indicators menu
indicatorparser = subparsers.add_parser('indicators', help='Indicator resource type')
indicatorparser.add_argument('-list', help='Retrieves a collection of all active Indicators.', action='store_true')

#Machines menu
machineparser = subparsers.add_parser('machines', help='Machine resource type')
machineparser.add_argument('-list', help='Retrieves a collection of Machines that have communicated with Microsoft Defender for Endpoint cloud.', action='store_true')

#Machines Actions menu
machineactionsparser = subparsers.add_parser('actions', help='Machine Action resource type')
machineactionsparser.add_argument('-offboard', help='Offboard device from Defender for Endpoint.', action='store_true')
machineactionsparser.add_argument('-quick', help='Initiate Microsoft Defender Antivirus quick scan on a device.', action='store_true')
machineactionsparser.add_argument('-full', help='Initiate Microsoft Defender Antivirus full scan on a device.', action='store_true')

#Recommendations menu
recommendationsparser = subparsers.add_parser('recommendations', help='Recommendation resource type')
recommendationsparser.add_argument('-list', help='Retrieves a collection of Machines that have communicated with Microsoft Defender for Endpoint cloud.', action='store_true')

#Software menu
softwareparser = subparsers.add_parser('software', help='Software resource type')
softwareparser.add_argument('-list', help='Retrieves the organization software inventory.', action='store_true')

#Vulnerabilities menu
vulnerabilitiesparser = subparsers.add_parser('vulnerabilities', help='vulnerability resource type')
vulnerabilitiesparser.add_argument('-list', help='Retrieves a list of all vulnerabilities.', action='store_true')

args = parser.parse_args()

if len(sys.argv) != 3:
    print('Not enough arguments. EX: python app.py alerts -list or python app.py alerts -h')
    parser.print_help()
else:
#Login token
    tenantid = input('Please enter your Tenant ID: ')
    appid = input('Please enter your Application ID: ')
    secret = getpass.getpass('Please enter your Application Secret:')
    new_token = gettoken.GetToken(tenantid, appid, secret)
    new_token.gettoken()
    token = new_token.aadToken

#List anything
    list_commands = ['alerts', 'investigations','indicators', 'machines', 'recommendations', 'software', 'vulnerabilities']       
    
    if args.Commands in list_commands:
        if args.list:
            new_list = list.List(token, args.Commands)
            new_list.list()
        else:
            parser.print_help()

#Actions
    elif args.Commands == 'actions':
        if args.offboard:
            filename = input('Please enter the CSV filename (export from MDE/Devices): ')
            comment = input('Comment (mandatory): ')
            new_csv = read.Csv(filename)
            new_csv.open()
            for ids in new_csv.list_ids:
                new_offboard_action = actions.Action(token, ids, comment, '')
                new_offboard_action.offboard()
        elif args.quick:
            filename = input('Please enter the CSV filename (export from MDE/Devices): ')
            comment = input('Comment (mandatory): ')
            new_csv = read.Csv(filename)
            new_csv.open()
            for ids in new_csv.list_ids:
                new_scan_action = actions.Action(token, ids, comment, 'Quick')
                new_scan_action.scan()
        elif args.full:
            filename = input('Please enter the CSV filename (export from MDE/Devices): ')
            comment = input('Comment (mandatory): ')
            new_csv = read.Csv(filename)
            new_csv.open()
            for ids in new_csv.list_ids:
                new_scan_action = actions.Action(token, ids, comment, 'Full')
                new_scan_action.scan()
        else:
            parser.print_help()

    else:
        parser.print_help()
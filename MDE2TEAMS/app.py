import getpass
import argparse
import time
from MDEAPI import gettoken
from MDEAPI import list
from TEAMS import send2teams

#menu argparser
parser = argparse.ArgumentParser(description='MDE4Teams = A tool to track MDE events in Teams', epilog='Original project created by Bruno Rodrigues - rodrigues.bruno@microsoft.com')
parser.add_argument('list', choices=['alerts', 'investigations', 'indicators', 'machines', 'machineactions', 'recommendations', 'Software', 'vulnerabilities'], help='Select which notifications to List in Teams')

args = parser.parse_args()

#Login token
try:
    tenantid = input('Please enter your Tenant ID: ')
    appid = input('Please enter your Application ID: ')
    secret = getpass.getpass('Please enter your Application Secret:')
    webhook = getpass.getpass('Please enter your webhook from Teams: ')
    new_token = gettoken.GetToken(tenantid, appid, secret)
    new_token.gettoken()
    token = new_token.aadToken
except Exception as e:
    print(e)

#Lists with no body API
#  
#First run
try:
    new_baseline = list.List(token, f'{args.list}')
    new_baseline.list()
    baseline_list = new_baseline.jsonResponse['value']
except Exception as e:
    print(e)

#Loop - keep running
while True:
    try:
        new_events = list.List(token, f'{args.list}')
        new_events.list()
        events_list = new_events.jsonResponse['value']
        if events_list == baseline_list:
            print(f'No new {args.list}')
        else:
            diff = [i for i in events_list if i not in baseline_list]
            message = f'{args.list} - {str(diff)}'
            new_message_teams = send2teams.Send2teams(webhook, message)
            new_message_teams.send2teams()
            print(f'{args.list} sent to Teams')
        update_baseline = list.List(token, f'{args.list}')
        update_baseline.list()
        baseline_list = update_baseline.jsonResponse['value']
        local_time = time.ctime()
        print(local_time)
        time.sleep(120)
    except Exception as e:
        print(e)
    
import getpass
import argparse
import time
from MDEAPI import gettoken
from MDEAPI import list
from TEAMS import send2teams

#menu argparser
parser = argparse.ArgumentParser(prog='app.py', description='MDE4Teams = A tool to track MDE events in Teams', epilog='Original project created by Bruno Rodrigues - rodrigues.bruno@microsoft.com')
parser.add_argument('list', choices=['alerts', 'investigations', 'indicators', 'machines', 'machineactions', 'recommendations', 'Software', 'vulnerabilities'], help='Select which notifications to List in Teams')

args = parser.parse_args()

#Login token
try:
    #tenantid = input('Please enter your Tenant ID: ')
    tenantid = '75b3e7f6-2e24-4fb0-8e84-ec9e587c8d4c'
    #appid = input('Please enter your Application ID: ')
    appid = '63b23291-8e11-4e1b-b102-9e5ad098af6e'
    #secret = getpass.getpass('Please enter your Application Secret:')
    secret = '4_U_S93E5MEYyomdw-Y1lV4.Ckw8y30l-1'
    #webhook = getpass.getpass('Please enter your webhook from Teams: ')
    webhook = 'https://microsoft.webhook.office.com/webhookb2/148071e4-ac99-4cd2-bfee-3571d8ef6bb9@72f988bf-86f1-41af-91ab-2d7cd011db47/IncomingWebhook/922241bcd32c41ec8b2f4f448b8da4ff/3171f984-4cb1-43cb-87a0-235e65fc8c84'
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

#infinite loop
while True:
    try:
        new_events = list.List(token, f'{args.list}')
        new_events.list()
        events_list = new_events.jsonResponse['value']
        if events_list == baseline_list:
            print(f'No new {args.list}')
        else:
            for dict in events_list:
                if dict not in baseline_list:
                    new_teams_message = send2teams.Send2teams(webhook, dict)
                    new_teams_message.send2teams()
                    print('Message sent to Teams Channel')
            update_baseline = list.List(token, f'{args.list}')
            update_baseline.list()
            baseline_list = update_baseline.jsonResponse['value']
        local_time = time.ctime()
        print(local_time)
        time.sleep(120)
    except Exception as e:
        print(e)
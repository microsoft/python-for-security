import os
import time
import getfileloop
import create_files
import listcompare
import teams

#program start
try:
    baselinefile = input('Please enter the baseline filename: ')
    webhook = input('Please enter the webhook for the Microsoft Teams channel: ')

    os.system(f'copy {baselinefile} .\\archieve\{baselinefile}')
    os.rename(baselinefile, f'downloads/{baselinefile}')

except Exception as e:
    print(e)

while True:
    #Download new file and replace old one in archieve
    try:
        getfileloop.Downloadloop.downloadloop()

    except Exception as e:
        print(f'{e} - no new file #{time.asctime(time.localtime(time.time()))}')

    #Create the files with subnets
    try:
        old_filenames = create_files.Createfile('archieve', 'compare_files_old')
        old_filenames.createfile()
        new_filenames = create_files.Createfile('downloads', 'compare_files_new')
        new_filenames.createfile()
    except Exception as e:
        print(e)

    #compare the files and send them to teams
    try:
        files = os.listdir('./compare_files_new')
        for filename in files:

            ActionGroup_new = listcompare.Listcompare('compare_files_new', filename)
            ActionGroup_old = listcompare.Listcompare('compare_files_old', filename)

            list_new = set(ActionGroup_new.compare())
            list_old = set(ActionGroup_old.compare())
            subnets_added = set(list_new) - set(list_old)
            subnets_removed = set(list_old) - set(list_new)

            if not subnets_added:
                continue
            elif not subnets_removed:
                continue
            else:
                send_teams_added = teams.Teams(webhook, f'subnets added to {filename}: {subnets_added}')
                send_teams_added.teams()
                print(f'Subnets added to {filename}: ')
                print(subnets_added)
                send_teams_removed = teams.Teams(webhook, f'subnets removed to {filename}: {subnets_removed}')
                send_teams_removed.teams()
                print(f'Subnets removed from {filename}: ')
                print(subnets_removed)
    except Exception as e:
        send_teams_created = teams.Teams(webhook, f'New group of subnets added - {filename}')
        send_teams_created.teams()
        print(f'New group of subnets added - {filename}')
    print('Waiting for new file...')
    time.sleep(28800)
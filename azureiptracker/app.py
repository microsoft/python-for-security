import os
import shutil
import time
import getfileloop
import create_files
import listcompare
import teams
import create_folders

#Create folders
downloads = create_folders.CreateFolder('downloads')
archieve = create_folders.CreateFolder('archieve')
compare_files_new = create_folders.CreateFolder('compare_files_new')
compare_files_old = create_folders.CreateFolder('compare_files_old')

try:
    downloads.createfolder()
except FileExistsError:
    print('Folder downloads already exists')
try:
    archieve.createfolder()
except FileExistsError:
    print('Folder archieve already exists')
try:
    compare_files_new.createfolder()
except FileExistsError:
    print('Folder compare_files_new already exists')
try:
    compare_files_old.createfolder()
except FileExistsError:
    print('Folder compare_files_old already exists')

#Get baseline to archieve
baseline_file = input('Enter the baseline filename: ')
shutil.move(f'./{baseline_file}', f'./archieve/{baseline_file}')

#Test Teams connectivity
webhook = input('Please enter your Microsoft Teams webhook link: ')
send_teams_test = teams.Teams(webhook, 'Azure IP Tracker is now reporting to your Teams Channel')
send_teams_test.teams()

#Loop non stop
while True:
    #Download new file and replace old one in archieve
    try:
        if not os.listdir('./downloads'):
            getfileloop.Downloadloop.downloadloop()
        else:
            getfileloop.Downloadloop.downloadcleanup()
            getfileloop.Downloadloop.downloadloop()
    except Exception as e:
        print(e)
        

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
    print(f'#{time.asctime(time.localtime(time.time()))} - Waiting for new file')
    time.sleep(28800)
import os

class CreateFolder:

    def __init__(self, folder):
        self.folder = folder

    def createfolder(self):
        os.mkdir(self.folder)

downloads = CreateFolder('downloads')
archieve = CreateFolder('archieve')
compare_files_new = CreateFolder('compare_files_new')
compare_files_old = CreateFolder('compare_files_old')

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
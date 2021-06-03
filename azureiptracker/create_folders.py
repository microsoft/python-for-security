import os

class CreateFolder:

    def __init__(self, folder):
        self.folder = folder

    def createfolder(self):
        os.mkdir(self.folder)
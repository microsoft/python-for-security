import os
import json

class Createfile:
    def __init__(self, read_dir, write_dir):
        self.read_dir = read_dir
        self.write_dir = write_dir

    def createfile(self):
        try:
            json_file = os.listdir(f'./{self.read_dir}')
            with open(f'./{self.read_dir}/{json_file[0]}') as js:
                data_new = json.load(js)
                for value in data_new['values']:
                    filename_new = value['name']
                    create_filename_new = open(f'./{self.write_dir}/{filename_new}', 'w')
                    for subnet in value['properties']['addressPrefixes']:
                        create_filename_new.writelines(f'\n{subnet}')
        except Exception as e:
            print(e)

old_filename = Createfile('downloads', 'compare_files_new')
old_filename.createfile()

new_filename = Createfile('archieve', 'compare_files_old')
new_filename.createfile()
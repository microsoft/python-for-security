import urllib.request
import time
import os

class Downloadloop:
        
    def downloadloop():             
        today = time.strftime('%Y%m%d')
        url = f'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_{today}.json'
        urllib.request.urlretrieve(url, f'./downloads/ServiceTags_Public_{today}.json')
        r = urllib.request.urlopen(url)
        print(f'ServiceTags_Public_{today}.json created #{time.asctime(time.localtime(time.time()))}')
        
    def downloadcleanup():   
        today = time.strftime('%Y%m%d')
        archievefoler = os.listdir('./archieve')
        for file in archievefoler:
            os.remove(f'./archieve/{file}')
        downloadfolder = os.listdir('./downloads')
        for file in downloadfolder:
            os.rename(f'downloads/{file}', f'archieve/{file}')
        os.replace(f'ServiceTags_Public_{today}.json', f'downloads/ServiceTags_Public_{today}.json')
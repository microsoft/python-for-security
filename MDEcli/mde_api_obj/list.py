import json
import urllib.request
import urllib.parse

class List:
    def __init__(self, token, url):
        self.token = token
        self.url = url

    def list(self):
        try:
            url = f"https://api.securitycenter.microsoft.com/api/{self.url}"
            headers = { 
                'Content-Type' : 'application/json',
                'Accept' : 'application/json',
                'Authorization' : "Bearer " + self.token
            }

            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req)
            jsonResponse = json.loads(response.read())
            listdict = jsonResponse['value']
            for alert in listdict:
                print(f'\n###{self.url}###')
                for key,value in alert.items():
                    print(f'{key}: {value}')
                print('###END###\n')
        except Exception as e:
            print(e)
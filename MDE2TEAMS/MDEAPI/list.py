import json
import urllib.request
import urllib.parse

class List:
    def __init__(self, token, url_construct):
        self.token = token
        self.url_construct = url_construct

    def list(self):
        url = f"https://api.securitycenter.microsoft.com/api/{self.url_construct}"
        headers = { 
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : "Bearer " + self.token
        }



        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        self.jsonResponse = json.loads(response.read())
        return self.jsonResponse
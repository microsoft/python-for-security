import json
import urllib.request
import urllib.parse

class Action:
    def __init__(self, token, id, comment, body2):
        self.token = token
        self.id = id
        self.comment = comment
        self.body2 = body2

    def offboard(self):
        try:
            url = f"https://api.securitycenter.microsoft.com/api/machines/{self.id}/offboard"
            headers = { 
                'Content-Type' : 'application/json',
                'Accept' : 'application/json',
                'Authorization' : "Bearer " + self.token
            }

            data = json.dumps({"Comment": self.comment}).encode("utf-8")

            req = urllib.request.Request(url, data, headers)
            response = urllib.request.urlopen(req)
            jsonResponse = json.loads(response.read())
            print(f'{jsonResponse["computerDnsName"]} - Machine ID {jsonResponse["machineId"]} as been offboarded')
        except Exception as e:
            print(e)
    
    def scan(self):
        try:
            url = f"https://api.securitycenter.microsoft.com/api/machines/{self.id}/runAntiVirusScan"
            headers = { 
                'Content-Type' : 'application/json',
                'Accept' : 'application/json',
                'Authorization' : "Bearer " + self.token
            }

            data = json.dumps({"Comment": self.comment, "ScanType": self.body2}).encode("utf-8")
            #data = str(json.dumps(body)).encode("utf-8")

            req = urllib.request.Request(url, data, headers)
            response = urllib.request.urlopen(req)
            jsonResponse = json.loads(response.read())
            print(f'{jsonResponse["computerDnsName"]} - Machine ID {jsonResponse["machineId"]} - {jsonResponse["type"]} ({jsonResponse["scope"]}) action started')
        except Exception as e:
            print(e)
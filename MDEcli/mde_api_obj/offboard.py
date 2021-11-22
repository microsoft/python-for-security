import json
import urllib.request
import urllib.parse

class Offboard:
    def __init__(self, token, id, comment):
        self.token = token
        self.id = id
        self.comment = comment

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
            print(jsonResponse)
        except Exception as e:
            print(e)
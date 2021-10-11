import json
import urllib.request
import urllib.parse

class GetToken:
    def __init__(self, tenantId, appId, appSecret):
        self.tenantId = tenantId
        self.appId = appId
        self.appSecret = appSecret

    def gettoken(self):

        url = "https://login.microsoftonline.com/%s/oauth2/token" % (self.tenantId)

        resourceAppIdUri = 'https://api.securitycenter.microsoft.com'

        body = {
            'resource' : resourceAppIdUri,
            'client_id' : self.appId,
            'client_secret' : self.appSecret,
            'grant_type' : 'client_credentials'
        }

        data = urllib.parse.urlencode(body).encode("utf-8")

        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        jsonResponse = json.loads(response.read())
        self.aadToken = jsonResponse["access_token"]
        return self.aadToken
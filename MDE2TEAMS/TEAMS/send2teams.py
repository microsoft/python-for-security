import pymsteams

class Send2teams:
    def __init__(self, webhook, message):
        self.webhook = webhook
        self.message = message

    def send2teams(self):
        myTeamsMessage = pymsteams.connectorcard(f"{self.webhook}")
        myTeamsMessage.text(f"{self.message}")
        myTeamsMessage.send()
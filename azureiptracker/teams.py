import pymsteams

class Teams:
    def __init__(self, webhook, message):
        self.webhook = webhook
        self.message = message

    def teams(self):
        myTeamsMessage = pymsteams.connectorcard(f"{self.webhook}")
        myTeamsMessage.text(f"{self.message}")
        myTeamsMessage.send()
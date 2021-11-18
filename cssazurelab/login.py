from azure.cli.core import get_default_cli

class Login:
    def login():
        try:
            get_default_cli().invoke(['az', 'login', '--use-device-code'])
        except Exception as e:
            print(e)
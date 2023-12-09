from flyingdisc.discordtypes import (
    ApplicationCommand,
    ClientCredentialsAccessTokenResponse,
)


class DiscordApplicationCommands:
    def __init__(self):
        self.commands = {}

    def update_commands(self, guilds: list[int], app_id: str, client_secret: str, token_endpoint: str):
        import requests

        grant = {"grant_type": "client_credentials", "scope": "applications.commands.update"}
        r = requests.post(token_endpoint, data=grant, auth=(app_id, client_secret))
        r.raise_for_status()
        creds = ClientCredentialsAccessTokenResponse(**r.json())

        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {creds.access_token}",
        }

        for guild in guilds:
            commands_url = f"https://discord.com/api/v10/applications/{app_id}/guilds/{guild}/commands"

            for command in self.commands.keys():
                r = requests.post(commands_url, headers=headers, json={
                    "name": self.commands[command]["name"],
                    "description": self.commands[command]["description"],
                    "type": self.commands[command]["type"],
                    "options": self.commands[command]["options"],
                })
                r.raise_for_status()


    def command(self, app_cmd: ApplicationCommand):
        def wrap(function):
            def wrapped(*args, **kwargs):
                response = function(*args, **kwargs)
                return response

            self.commands[app_cmd.name] = {
                "function": wrapped,
                "name": app_cmd.name,
                "description": app_cmd.description,
                "type": app_cmd.type,
                "options": app_cmd.options,
            }

            return wrapped

        return wrap

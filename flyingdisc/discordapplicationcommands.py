from flyingdisc.discordtypes import (
    ApplicationCommand,
)

class DiscordApplicationCommands():
    def __init__(self):
        self.commands = {}

    def command(self, app_cmd: ApplicationCommand):
        def wrap(function):
            def wrapped(*args, **kwargs):
                response = function(*args, **kwargs)
                return response

            self.commands['name'] = {
                "function": wrapped,
                "name": app_cmd.name,
                "description": app_cmd.description,
                "type": app_cmd.type,
                "options": app_cmd.options,
            }

            return wrapped

        return wrap

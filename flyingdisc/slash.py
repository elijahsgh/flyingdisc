from flyingdisc.discordtypes import (
    ApplicationCommandType,
    ApplicationCommandInteractionDataOption,
)

class Slash:
    def __init__(self):
        self.commands = {}

    def command(
        self,
        name: str,
        description: str,
        type: ApplicationCommandType = ApplicationCommandType.CHAT_INPUT,
        options: ApplicationCommandInteractionDataOption = None,
    ):
        def wrap(function):
            def wrapped(*args, **kwargs):
                response = function(*args, **kwargs)
                return response

            self.commands[name] = {
                "function": wrapped,
                "name": name,
                "description": description,
                "type": type,
                "options": options,
            }

            return wrapped

        return wrap

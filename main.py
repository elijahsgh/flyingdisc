from flyingdisc import DiscordApplicationCommands
from flyingdisc.utils import DiscordSignedRequest

from flyingdisc.discordtypes import (
    ApplicationCommand,
    Interaction,
    InteractionResponse,
    InteractionCallbackType,
    CommandCallbackDataFlags,
)

interactions = DiscordApplicationCommands()


@interactions.command(ApplicationCommand(name="hello", description="Hello world"))
def command_hello(interaction: Interaction) -> InteractionResponse:
    return InteractionResponse(
        type=InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
        data={
            "flags": CommandCallbackDataFlags.EPHEMERAL,
            "content": "Hello",
        },
    )

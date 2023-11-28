# Assembled from https://discord.com/developers/docs/interactions/slash-commands on 2021-04-05
from __future__ import annotations

from enum import Enum
from xmlrpc.client import Boolean
from pydantic import BaseModel, ConfigDict, Field, StrictInt

from typing import Any, Dict, List, Optional


class ApplicationCommandOptionType(int, Enum):
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8


class InteractionType(int, Enum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPELTE = 4
    MODAL_SUBMIT = 5


class InteractionCallbackType(int, Enum):
    PONG = 1
    ACKNOWLEDGE = 2
    CHANNELMESSAGE = 3
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9


class AllowedMentionType(str, Enum):
    ROLE = "roles"
    USER = "users"
    EVERYONE = "everyone"


class NitroType(int, Enum):
    NONE = 0
    CLASSIC = 1
    NITRO = 2


class UserFlags(int, Enum):
    NONE = 0
    EMPLOYEE = 1 << 0
    PARTNERED = 1 << 1
    HYPESQUAD_EVENTS = 1 << 2
    BUGHUNTER_LEVEL1 = 1 << 3
    HOUSE_BRAVERY = 1 << 6
    HOUSE_BRILLIANCE = 1 << 7
    HOUSE_BALANCE = 1 << 8
    EARLY_SUPPORTER = 1 << 9
    TEAM_USER = 1 << 10
    SYSTEM = 1 << 12
    BUGHUTNER_LEVEL2 = 1 << 14
    VERIFIED_BOT = 1 << 16
    EARLY_VERIFIED_BOT_DEVELOPER = 1 << 17


class EmbedFooter(BaseModel):
    text: str
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]


class EmbedImage(BaseModel):
    url: Optional[str]
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]


class EmbedThumbnail(BaseModel):
    url: Optional[str]
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]


class EmbedVideo(BaseModel):
    url: Optional[str]
    proxy_url: Optional[str]
    height: Optional[int]
    width: Optional[int]


class EmbedProvider(BaseModel):
    name: Optional[str]
    url: Optional[str]


class EmbedAuthor(BaseModel):
    name: Optional[str]
    url: Optional[str]
    icon_url: Optional[str]
    proxy_icon_url: Optional[str]


class EmbedField(BaseModel):
    name: str
    value: str
    inline: Optional[bool]


class EmbedObject(BaseModel):
    title: Optional[str]
    type: str = "rich"
    description: Optional[str]
    url: Optional[str]
    timestamp: Optional[str]  # TODO: Make this a real ISO8601 timestamp type
    color: Optional[int]
    footer: Optional[EmbedFooter]
    image: Optional[EmbedImage]
    thumbnail: Optional[EmbedThumbnail]
    video: Optional[EmbedVideo]
    provider: Optional[EmbedProvider]
    author: Optional[EmbedAuthor]
    fields_: Optional[List[EmbedField]] = Field(..., alias="fields")


class AllowedMentions(BaseModel):
    parse: List[AllowedMentionType]
    roles: List[int]
    users: List[int]
    replied_user: bool = False


class InteractionApplicationCommandCallbackDataFlags(int, Enum):
    EPHEMERAL = 64


# Alias
class CommandCallbackDataFlags(int, Enum):
    EPHEMERAL = 64


class Component(BaseModel):
    type: ComponentTypes
    components: Optional[List[Component]]
    label: Optional[str]
    style: Optional[int]
    custom_id: Optional[str]
    disabled: Optional[Boolean]
    emoji: Optional[Any]  # emoji type not implemented
    label: Optional[str]
    max_values: Optional[int]
    min_values: Optional[int]
    url: Optional[str]
    options: Optional[List[Any]]


class InteractionApplicationCommandCallbackData(BaseModel):
    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return super().model_dump(*args, **kwargs)

    tts: Optional[bool] = False
    content: Optional[str] = None
    embeds: Optional[List[EmbedObject]]
    allowed_mentions: Optional[AllowedMentions]
    flags: Optional[CommandCallbackDataFlags]  # Set to 64 for user-only message
    components: Optional[List[Component]]  # TODO: Type not implemented
    attachments: Optional[List[Any]]  # TODO: Type not implemeneted

    # for modals
    custom_id: Optional[str] = None
    title: Optional[str] = None


# Alias
class CommandCallbackData(InteractionApplicationCommandCallbackData):
    pass


class InteractionResponse(BaseModel):
    type: Optional[
        InteractionCallbackType
    ] = InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE
    data: Optional[InteractionApplicationCommandCallbackData]


class User(BaseModel):
    id: int
    username: str
    discriminator: str
    avatar: str = None
    bot: Optional[bool]
    system: Optional[bool]
    mfa_enabled: Optional[bool]
    locale: Optional[str]
    verified: Optional[bool]
    email: Optional[str]
    flags: Optional[int]
    premium_type: Optional[NitroType]
    public_flags: Optional[int]


class MessageReference(BaseModel):
    message_id: Optional[int]
    channel_id: Optional[int]
    guild_id: Optional[int]
    fail_if_not_exists: Optional[Boolean]


class Message(BaseModel):
    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return super().dict(*args, **kwargs)

    id: Optional[int]
    channel_id: Optional[int]
    guild_id: Optional[int]
    author: Optional[User]  # user
    member: Optional[Any]  # partial Guild Member object
    content: Optional[str]
    timestamp: Optional[str]  # ISO8601 timestamp
    edited_timestamp: Optional[str] = None  # ISO8601 timestamp
    tts: Optional[Boolean]
    mention_everyone: Optional[Boolean]
    mentions: Optional[List[Any]]
    mention_roles: Optional[List[Any]]
    mention_channels: Optional[List[Any]]
    attachments: Optional[List[Any]]
    embeds: Optional[List[Any]]
    reactions: Optional[List[Any]]
    nonce: Optional[str]
    pinned: Optional[bool]
    webhook_id: Optional[int]
    type: Optional[int]
    activity: Optional[Any]
    application: Optional[Any]
    application_id: Optional[int]
    message_reference: Optional[Any]
    flags: Optional[int]
    referenced_message: Optional[Any]
    message_reference: Optional[MessageReference]
    interaction: Optional[Interaction]
    thread: Optional[Any]
    components: Optional[List[Component]]
    sticker_items: Optional[List[Any]]
    stickers: Optional[List[Any]]
    interaction: Optional[Interaction]


class GuildMember(BaseModel):
    user: Optional[User]
    nick: Optional[str]
    roles: List[int]
    joined_at: str  # TODO: This is ISO8601 timestamp
    premium_since: Optional[str]  # TODO: This is ISO8601 timestamp
    deaf: bool
    mute: bool
    pending: Optional[bool]
    permissions: Optional[str]


class ApplicationCommandInteractionDataOption(BaseModel):
    name: str
    value: Any
    type: ApplicationCommandOptionType
    options: Optional[List[ApplicationCommandInteractionDataOption]]


class ResolvedData(BaseModel):
    #  Unimplemented, see https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure
    pass


class ApplicationCommandInteractionData(BaseModel):
    id: Optional[int]
    name: Optional[str]
    options: Optional[List[ApplicationCommandInteractionDataOption]]

    # for message components
    custom_id: Optional[str]
    component_type: Optional[ComponentTypes]
    values: Optional[List[str]]

    # User Commands and Message Commands, see ResolvedData
    resolved: Optional[Dict]


class SelectOption(BaseModel):
    label: str
    value: str
    description: Optional[str]
    # Needs partial Emoji
    emoji: Optional[Any]
    default: Optional[Boolean]


class Interaction(BaseModel):
    id: int
    name: Optional[str]
    application_id: int = None
    type: InteractionType
    data: Optional[ApplicationCommandInteractionData]
    guild_id: Optional[int]
    channel_id: Optional[int]
    member: Optional[GuildMember]
    user: Optional[User]
    token: str = None
    version: int = 1
    message: Optional[Message]
    locale: Optional[Any]
    guild_locale: Optional[Any]


class ApplicationCommandOptionChoice(BaseModel):
    name: str
    value: Any


class ApplicationCommandOption(BaseModel):
    type: ApplicationCommandOptionType
    name: str
    description: str
    required: Optional[Boolean]
    choices: Optional[List[ApplicationCommandOptionChoice]]
    options: Optional[List[ApplicationCommandOption]] = None


class ApplicationCommandType(int, Enum):
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3


class ApplicationCommand(BaseModel):
    name: str
    description: str

    id: Optional[int] = None
    type: Optional[ApplicationCommandType] = 1
    application_id: Optional[int] = None
    guild_id: Optional[int] = None
    name_localizations: Optional[Any] = None  # Not implemented
    description_localizations: Optional[Any] = None  # Not implemeneted
    options: Optional[List[ApplicationCommandOption]] = None
    default_member_permissions: Optional[str] = 0  # Limit to admins by default
    dm_permissions: Optional[Boolean] = None
    version: Optional[int] = 0


class ClientCredentialsAccessTokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    scope: str


class ComponentTypes(int, Enum):
    ACTION_ROW = 1
    BUTTON = 2
    SELECT_MENU = 3
    TEXT_INPUT = 4


class ButtonStyles(int, Enum):
    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    DANGER = 4
    LINK = 5


class ApplicationRoleConnectionMetadataType(int, Enum):
    INTEGER_LESS_THAN_OR_EQUAL = 1
    INTEGER_GREATER_THAN_OR_EQUAL = 2
    INTEGER_EQUAL = 3
    INTEGER_NOT_EQUAL = 4
    DATETIME_LESS_THAN_OR_EQUAL = 5
    DATETIME_GREATER_THAN_OR_EQUAL = 6
    BOOLEAN_EQUAL = 7
    BOOLEAN_NOT_EQUAL = 8


class ApplicationRoleConnectionMetadata(BaseModel):
    type: ApplicationRoleConnectionMetadataType
    key: str
    name: str
    name_localizations: Optional[dict]
    description: str
    description_localizations: Optional[dict]


Message.model_rebuild()
ApplicationCommandInteractionData.model_rebuild()
Component.model_rebuild()
ApplicationCommandInteractionDataOption.model_rebuild()

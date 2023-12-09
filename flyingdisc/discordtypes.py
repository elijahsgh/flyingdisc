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
    icon_url: Optional[str] = None
    proxy_icon_url: Optional[str] = None


class EmbedImage(BaseModel):
    url: Optional[str] = None
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None


class EmbedThumbnail(BaseModel):
    url: Optional[str] = None
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None


class EmbedVideo(BaseModel):
    url: Optional[str] = None
    proxy_url: Optional[str] = None
    height: Optional[int] = None
    width: Optional[int] = None


class EmbedProvider(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None


class EmbedAuthor(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    icon_url: Optional[str] = None
    proxy_icon_url: Optional[str] = None


class EmbedField(BaseModel):
    name: str
    value: str
    inline: Optional[bool] = None


class EmbedObject(BaseModel):
    title: Optional[str] = None
    type: str = "rich"
    description: Optional[str] = None
    url: Optional[str] = None
    timestamp: Optional[str] = None # TODO: Make this a real ISO8601 timestamp type
    color: Optional[int] = None
    footer: Optional[EmbedFooter] = None
    image: Optional[EmbedImage] = None
    thumbnail: Optional[EmbedThumbnail] = None
    video: Optional[EmbedVideo] = None
    provider: Optional[EmbedProvider] = None
    author: Optional[EmbedAuthor] = None
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
    components: Optional[List[Component]] = None
    label: Optional[str] = None
    style: Optional[int] = None
    custom_id: Optional[str] = None
    disabled: Optional[Boolean] = None
    emoji: Optional[Any] = None  # emoji type not implemented
    label: Optional[str] = None
    max_values: Optional[int] = None
    min_values: Optional[int] = None
    url: Optional[str] = None
    options: Optional[List[Any]] = None


class InteractionApplicationCommandCallbackData(BaseModel):
    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return super().model_dump(*args, **kwargs)

    tts: Optional[bool] = False
    content: Optional[str] = None
    embeds: Optional[List[EmbedObject]] = None
    allowed_mentions: Optional[AllowedMentions] = None
    flags: Optional[CommandCallbackDataFlags] = None  # Set to 64 for user-only message
    components: Optional[List[Component]] = None  # TODO: Type not implemented
    attachments: Optional[List[Any]] = None  # TODO: Type not implemeneted

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
    data: Optional[InteractionApplicationCommandCallbackData] = None


class User(BaseModel):
    id: int
    username: str
    discriminator: str
    avatar: str = None
    bot: Optional[bool] = None 
    system: Optional[bool] = None
    mfa_enabled: Optional[bool] = None
    locale: Optional[str] = None
    verified: Optional[bool] = None
    email: Optional[str] = None
    flags: Optional[int] = None
    premium_type: Optional[NitroType] = None
    public_flags: Optional[int] = None


class MessageReference(BaseModel):
    message_id: Optional[int] = None
    channel_id: Optional[int] = None
    guild_id: Optional[int] = None
    fail_if_not_exists: Optional[Boolean] = None


class Message(BaseModel):
    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return super().dict(*args, **kwargs)

    id: Optional[int]
    channel_id: Optional[int] = None
    guild_id: Optional[int] = None
    author: Optional[User] = None  # user
    member: Optional[Any] = None  # partial Guild Member object
    content: Optional[str] = None
    timestamp: Optional[str] = None  # ISO8601 timestamp
    edited_timestamp: Optional[str] = None  # ISO8601 timestamp
    tts: Optional[Boolean] = None
    mention_everyone: Optional[Boolean] = None
    mentions: Optional[List[Any]] = None
    mention_roles: Optional[List[Any]] = None
    mention_channels: Optional[List[Any]] = None
    attachments: Optional[List[Any]] = None
    embeds: Optional[List[Any]] = None
    reactions: Optional[List[Any]] = None
    nonce: Optional[str] = None
    pinned: Optional[bool] = None
    webhook_id: Optional[int] = None
    type: Optional[int] = None
    activity: Optional[Any] = None
    application: Optional[Any] = None
    application_id: Optional[int] = None
    message_reference: Optional[Any] = None
    flags: Optional[int] = None
    referenced_message: Optional[Any] = None
    message_reference: Optional[MessageReference] = None
    interaction: Optional[Interaction] = None
    thread: Optional[Any] = None
    components: Optional[List[Component]] = None
    sticker_items: Optional[List[Any]] = None
    stickers: Optional[List[Any]] = None
    interaction: Optional[Interaction] = None


class GuildMember(BaseModel):
    user: Optional[User] = None
    nick: Optional[str] = None
    roles: List[int]
    joined_at: str  # TODO: This is ISO8601 timestamp
    premium_since: Optional[str] = None  # TODO: This is ISO8601 timestamp
    deaf: bool
    mute: bool
    pending: Optional[bool] = None
    permissions: Optional[str] = None


class ApplicationCommandInteractionDataOption(BaseModel):
    name: str
    value: Any
    type: ApplicationCommandOptionType
    options: Optional[List[ApplicationCommandInteractionDataOption]] = None


class ResolvedData(BaseModel):
    #  Unimplemented, see https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure
    pass


class ApplicationCommandInteractionData(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    options: Optional[List[ApplicationCommandInteractionDataOption]] = None

    # for message components
    custom_id: Optional[str] = None
    component_type: Optional[ComponentTypes] = None
    values: Optional[List[str]] = None

    # User Commands and Message Commands, see ResolvedData
    resolved: Optional[Dict] = None


class SelectOption(BaseModel):
    label: str
    value: str
    description: Optional[str] = None
    # Needs partial Emoji
    emoji: Optional[Any] = None
    default: Optional[Boolean] = None


class Interaction(BaseModel):
    id: int
    name: Optional[str] = None
    application_id: int = None
    type: InteractionType
    data: Optional[ApplicationCommandInteractionData] = None
    guild_id: Optional[int] = None
    channel_id: Optional[int] = None
    member: Optional[GuildMember] = None
    user: Optional[User] = None
    token: str = None
    version: int = 1
    message: Optional[Message] = None
    locale: Optional[Any] = None
    guild_locale: Optional[Any] = None


class ApplicationCommandOptionChoice(BaseModel):
    name: str
    value: Any


class ApplicationCommandOption(BaseModel):
    type: ApplicationCommandOptionType
    name: str
    description: str
    required: Optional[Boolean] = None
    choices: Optional[List[ApplicationCommandOptionChoice]] = None
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
    name_localizations: Optional[dict] = None
    description: str
    description_localizations: Optional[dict] = None


Message.model_rebuild()
ApplicationCommandInteractionData.model_rebuild()
Component.model_rebuild()
ApplicationCommandInteractionDataOption.model_rebuild()

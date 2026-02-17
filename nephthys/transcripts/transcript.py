from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator


class Transcript(BaseModel):
    """Class to hold all the transcript messages and links used in the bot."""

    class Config:
        """Configuration for the Pydantic model."""

        extra = "forbid"

    program_name: str = Field(
        default="Hackatime", description="Name of the program"
    )
    program_owner: str = Field(
        default="U054VC2KM9P",
        description="Slack ID of the support manager",
    )
    help_channel: str = Field(
        default="",
        description="Slack channel ID for help requests",
    )
    ticket_channel: str = Field(
        default="",
        description="Slack channel ID for ticket creation",
    )
    team_channel: str = Field(
        default="",
        description="Slack channel ID for team discussions and stats",
    )
    ticket_reopen: str = Field(
        default="",
        description="Message when ticket is reopened",
    )

    @property
    def program_snake_case(self) -> str:
        """Snake case version of the program name."""
        return self.program_name.lower().replace(" ", "_")

    summer_help_channel: str = Field(
        default="C091D312J85", description="Summer help channel ID"
    )

    first_ticket_create: str = Field(
        default="", description="Message for first-time ticket creators"
    )

    ticket_create: str = Field(default="", description="Message for ticket creation")

    resolve_ticket_button: str = Field(
        default="Mark as resolved",
        description="Text for the green resolve-ticket button",
    )

    ticket_resolve: str = Field(
        default="", description="Message when ticket is resolved"
    )

    ticket_resolve_stale: str = Field(
        default="",
        description="Message when ticket is resolved due to being stale",
    )

    thread_broadcast_delete: str = Field(
        default="hey! please keep your messages *all in one thread* to make it easier to read! i've gone ahead and removed that message from the channel for ya :D",
    )

    dev_macro: str = Field(
        default="hey, (user)! this looks like a development question. please head over to #hackatime-dev for help with this!",
        description="Message to be sent when the dev macro is used",
    )

    fraud_macro: str = Field(
        default="hiya (user)! Would you mind directing any fraud related queries to <@U091HC53CE8>? :rac_cute:\n\nit'll keep your case confidential and make it easier for the fraud team to keep track of!",
        description="Message to be sent when the fraud macro is used",
    )

    not_allowed_channel: str = Field(
        default="", description="Message for unauthorized channel access"
    )

    @model_validator(mode="after")
    def set_default_messages(self):
        """Set default values for messages that reference other fields"""
        if not self.first_ticket_create:
            self.first_ticket_create = """hey (user)! thanks for posting in Hackatime support. someone should be along to help you soon.
if your question gets solved before then, please hit the button below to mark it as resolved.
"""

        if not self.ticket_create:
            self.ticket_create = """someone should be along to help you soon.
if your question has already been solved, please hit the button below to mark it as resolved :D
"""

        if not self.ticket_resolve:
            self.ticket_resolve = """oh, oh! it looks like this post has been marked as resolved by <@{user_id}>!
if you have more questions, please make a new post in this channel and someone will help you out ^-^
"""

        if not self.ticket_resolve_stale:
            self.ticket_resolve_stale = """:rac_nooo: it looks like this post is a bit old!
if you still need help, please make a new post in this channel and someone will help you out! ^~^
"""

        if not self.not_allowed_channel:
            self.not_allowed_channel = f"heya, it looks like you're not supposed to be in that channel, pls talk to <@{self.program_owner}> if that's wrong"

        if not self.ticket_reopen:
            self.ticket_reopen = "hey hey! it looks like <@{helper_slack_id}> has reopened this post! someone'll be with you shortly, ty!"

        return self

from nephthys.macros.types import Macro
from nephthys.utils.env import env
from nephthys.utils.slack_user import get_user_profile
from nephthys.utils.ticket_methods import reply_to_ticket


class Dev(Macro):
    name = "dev"

    async def run(self, ticket, helper, **kwargs):
        """
        Points users to the #hackatime-dev channel.
        """
        sender = await env.db.user.find_first(where={"id": ticket.openedById})
        if not sender:
            return
        user = await get_user_profile(sender.slackId)
        await reply_to_ticket(
            text=env.transcript.dev_macro.replace("(user)", user.display_name()),
            ticket=ticket,
            client=env.slack_client,
        )

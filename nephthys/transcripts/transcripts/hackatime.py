from nephthys.transcripts.transcript import Transcript


class Hackatime(Transcript):
    """Transcript for Hackatime support."""

    program_name: str = "Hackatime"
    program_owner: str = "U054VC2KM9P"

    first_ticket_create: str = """
hey (user)! thanks for posting in Hackatime support.
someone from the team will be with you soon.
if your question is solved before then, please hit the button below to mark it as resolved.
"""

    ticket_create: str = """
someone from the team will reply soon.
if your question has already been solved, please hit the button below to mark it as resolved :D
"""

    ticket_resolve: str = """
this post has been marked as resolved by <@{user_id}>.
if you need more help, make a new post in this channel and we can jump back in.
"""

    ticket_resolve_stale: str = """
:rac_nooo: this post looks a bit old.
if you still need help, please make a new post in this channel and someone will help you out.
"""

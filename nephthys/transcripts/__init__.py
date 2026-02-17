from typing import List
from typing import Type

from nephthys.transcripts.transcript import Transcript
from nephthys.transcripts.transcripts.hackatime import Hackatime


transcripts: List[Type[Transcript]] = [
    Hackatime,
]

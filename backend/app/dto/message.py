from dataclasses import dataclass


@dataclass
class MessageDto:
    success: bool
    message: str

from dataclasses import dataclass
import uuid


@dataclass
class AuthorId:
    value: uuid

    def __init__(self, value: uuid):
        if value is None:
            raise Exception("UserId cannot be None")
        self.value = value

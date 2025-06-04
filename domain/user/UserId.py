from dataclasses import dataclass
import uuid


@dataclass
class UserId:
    value: uuid

    def __init__(self, value: uuid):
        if value is None:
            raise Exception("UserId cannot be None")
        self.value = value

    @classmethod
    def new(cls) -> "UserId":
        return cls(uuid.uuid4())

from dataclasses import dataclass
import uuid


@dataclass
class CommentId:
    value: uuid

    def __init__(self, value: uuid):
        if value is None:
            raise Exception("CommentId cannot be None")
        self.value = value

    @classmethod
    def new(cls) -> "CommentId":
        return cls(uuid.uuid4())

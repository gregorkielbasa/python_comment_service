from dataclasses import dataclass
import uuid


@dataclass
class CommentText:
    value: str

    def __init__(self, value: str):
        if value is None:
            raise Exception("CommentText cannot be None")
        if len(value) > 100:
            raise Exception("CommentText cannot be longer than 100 characters")
        self.value = value.strip()

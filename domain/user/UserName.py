from dataclasses import dataclass


@dataclass
class UserName:
    value: str

    def __init__(self, value: str):
        if value is None:
            raise Exception("UserName cannot be None")
        self.value = value

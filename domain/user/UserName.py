from dataclasses import dataclass


@dataclass
class UserName:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        if first_name is None:
            raise Exception("First Name cannot be None")
        if len(first_name) > 25:
            raise Exception("First Name cannot be more than 25 characters")
        self.first_name = first_name.strip()
        if last_name is None:
            raise Exception("Last Name cannot be None")
        if len(last_name) > 25:
            raise Exception("Last Name cannot be more than 25 characters")
        self.last_name = last_name.strip()
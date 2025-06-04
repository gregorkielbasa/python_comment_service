from dataclasses import dataclass


@dataclass
class UserEmail:
    value: str

    def __init__(self, value: str) -> None:
        if value is None:
            raise Exception("eMAil cannot be None")
        self.value = value

    @classmethod
    def new(cls, first_name: str, last_name: str) -> "UserEmail":
        if first_name is None or last_name is None:
            raise Exception("eMail cannot be created with None values")
        email: str = "{first_name}.{last_name}@emial.com".format(first_name=first_name, last_name=last_name)
        return cls(email)
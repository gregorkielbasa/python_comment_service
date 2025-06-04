from domain.user.UserId import UserId
from domain.user.UserName import UserName


class User:
    user_id: UserId
    username: UserName

    @classmethod
    def new(cls, user_name: UserName) -> "User":
        return cls(UserId.new(), user_name)

    def __init__(self, user_id: UserId, username: UserName):
        self.__set_id(user_id)
        self.__set_name(username)

    def rename(self, new_name: UserName) -> None:
        self.__set_name(new_name)

    def __set_id(self, user_id: UserId) -> None:
        if user_id is None is None:
            raise Exception("UserId cannot be None")
        self.user_id: UserId = user_id

    def __set_name(self, username: UserName):
        if username is None:
            raise Exception("UserName cannot be None")
        self.username: UserName = username

    def __repr__(self):
        return "User(id={}, name={})".format(self.user_id, self.username)

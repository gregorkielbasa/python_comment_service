from domain.user.UserEmail import UserEmail
from domain.user.UserId import UserId
from domain.user.UserName import UserName


class User:
    user_id: UserId
    username: UserName
    email: UserEmail

    @classmethod
    def new(cls, user_name: UserName) -> "User":
        user_email = UserEmail.new(user_name.first_name, user_name.last_name)
        return cls(UserId.new(), user_name, user_email)

    def __init__(self, user_id: UserId, username: UserName, email: UserEmail):
        self.__set_id(user_id)
        self.__set_name(username)
        self.__set_email(email)

    def __set_id(self, user_id: UserId) -> None:
        if user_id is None is None:
            raise Exception("UserId cannot be None")
        self.user_id: UserId = user_id

    def __set_name(self, username: UserName) -> None:
        if username is None:
            raise Exception("UserName cannot be None")
        self.username: UserName = username

    def __set_email(self, email: UserEmail) -> None:
        if email is None:
            raise Exception("UserEmail cannot be None")
        self.email: UserEmail = email

    def __repr__(self):
        return "User(id={}, name={}, email={})".format(self.user_id, self.username, self.email)

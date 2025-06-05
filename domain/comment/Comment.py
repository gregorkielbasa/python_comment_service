from domain.comment import AuthorId
from domain.comment.CommentId import CommentId
from domain.comment.CommentText import CommentText


class Comment:
    comment_id: CommentId
    author_id: AuthorId
    text: CommentText

    @classmethod
    def new(cls, author_id: AuthorId, text: CommentText) -> "Comment":
        comment_id = CommentId.new()
        return cls(comment_id, author_id, text)


    def __init__(self, comment_id: CommentId, author_id: AuthorId, text: CommentText):
        self.__set_author_id(author_id)
        self.__set_comment_id(comment_id)
        self.__set_text(text)

    def __set_author_id(self, author_id: AuthorId):
        if author_id is None:
            raise Exception("Author id cannot be None")
        self.author_id = author_id

    def __set_comment_id(self, comment_id: CommentId):
        if comment_id is None:
            raise Exception("Comment id cannot be None")
        self.comment_id = comment_id

    def __set_text(self, comment_text: CommentText):
        if comment_text is None:
            raise Exception("Comment text cannot be None")
        self.text = comment_text
        
    def __repr__(self):
        return ("Comment:(comment_id={}, author_id={}, text={})"
                .format(self.comment_id, self.author_id, self.text))
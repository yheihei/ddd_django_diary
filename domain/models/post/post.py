from domain.models.post.post_id import PostId
from domain.models.post.post_title import PostTitle
from domain.models.post.post_body import PostBody


class Post:
    def __init__(self, post_id: PostId, post_title: PostTitle, post_body: PostBody) -> None:
        self.__post_id = post_id
        self.__post_title = post_title
        self.__post_body = post_body

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__post_id == self.__post_id
        return False

    @property
    def id(self) -> PostId:
        return self.__post_id

    @property
    def title(self) -> PostTitle:
        return self.__post_title

    @property
    def body(self) -> PostBody:
        return self.__post_body

    def change_title(self, title: str) -> None:
        self.__post_title = PostTitle(title)

    def change_body(self, body: str) -> None:
        self.__post_body = PostBody(body)

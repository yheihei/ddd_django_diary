from domain.models.base.base_value_object import BaseValueObject


class PostTitle(BaseValueObject):
    def __init__(self, value: str) -> None:
        if type(value) is not str:
            raise ValueError('str以外は入力できません')
        if not value:
            raise ValueError('タイトルは空白にできません')
        if len(value) > 4096:
            raise ValueError('タイトルは4096文字以下です')
        super().__init__(value)

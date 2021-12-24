from domain.models.base.base_value_object import BaseValueObject


class PostBody(BaseValueObject):
    def __init__(self, value: str) -> None:
        if type(value) is not str:
            raise ValueError('str以外は入力できません')
        super().__init__(value)


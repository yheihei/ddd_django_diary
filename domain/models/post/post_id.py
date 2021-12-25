from domain.models.base.base_value_object import BaseValueObject


class PostId(BaseValueObject):
    def __init__(self, value: int) -> None:
        if type(value) is not int:
            raise ValueError('数値以外は入力できません')
        super().__init__(value)


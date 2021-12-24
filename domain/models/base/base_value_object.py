class BaseValueObject:
    def __init__(self, value) -> None:
        self.__value = value

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__value == other.__value
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
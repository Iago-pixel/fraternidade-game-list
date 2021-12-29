class InvalidFormatError(Exception):
    def __init__(self, msg: str) -> None:
        self.message = {"msg": msg}
        super().__init__(msg)


class InvalidStringSizeError(Exception):
    def __init__(self, msg) -> None:
        self.message = {"msg": msg}
        super().__init__(msg)


class InvalidNumberError(Exception):
    def __init__(self, msg) -> None:
        self.message = {"msg": msg}
        super().__init__(msg)

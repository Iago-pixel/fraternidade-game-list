class AlreadyExistsError(Exception):
    def __init__(self, msg: str) -> None:
        self.message = {"msg": msg}
        super().__init__(msg)

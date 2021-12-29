class InvalidKeyError(Exception):
    def __init__(self, err) -> None:
        self.message = err

from app.exc.type_exceptions import IncorrectTypeError
from app.exc.key_exeptions import InvalidKeyError
from app.exc.format_exceptions import InvalidStringSizeError


def validate_type(key: str, value, expected_type):
    types = {
        str: "string",
        int: "integer",
        float: "float",
        list: "list",
        dict: "dictionary",
        tuple: "tuple",
        bool: "boolean",
    }

    if not isinstance(value, expected_type):
        received_type = "null"
        expected_type_str = types[expected_type]

        if value != None:
            received_type = types[type(value)]

        raise IncorrectTypeError(
            f"Expected {expected_type_str} in {key}, but received {received_type}"
        )


def validate_keys(valid_keys: list, received_keys: list, required_keys: list = []):
    """Raise erro case have invalid keys or missing keys

    Args:
        valid_keys(list): keys that can be sent on request
        received_keys(list): keys that were sent on request
        required_keys(list): keys that are mandatory on request
    """
    invalid_keys: list = []
    missing_keys: list = []

    for key in received_keys:
        if not key in valid_keys:
            invalid_keys.append(key)

    if required_keys:
        for key in required_keys:
            if not key in received_keys:
                missing_keys.append(key)

    if missing_keys:
        err = {"required_keys": required_keys, "missing_keys": missing_keys}
        raise InvalidKeyError(err)
    elif invalid_keys:
        err = {"valid_keys": valid_keys, "invalid_keys": invalid_keys}
        raise InvalidKeyError(err)


def validate_string_size(key: str, value: str, max_size: int):
    """Raise a error if the size exceeds the maximum

    Args:
        key(str): key that will be validated
        value(str): value that will be validated
        max_size(int): max size"""
    if len(value) > max_size:
        raise InvalidStringSizeError(f"{key} accepts a maximum of {max_size} catacters")

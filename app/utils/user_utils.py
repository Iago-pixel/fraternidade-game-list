from app.models.user_model import User
from app.utils.generics_utils import validate_keys

from app.exc.already_exists_exceptions import AlreadyExistsError


def user_unique_value_already_exists(data: dict):
    """Raise a error if user name and/or user email already exists

    Args:
        data(dict): resquest data"""
    email = None
    name = None
    if "email" in data:
        email = data["email"]
    if "name" in data:
        name = data["name"]

    if isinstance(name, str) and isinstance(email, str):
        already_exists = ""

        user_this_email = None
        user_this_name = None
        if email:
            user_this_email = User.query.filter_by(email=email).first()

            if user_this_email:
                already_exists = "email"

        if name:
            user_this_name = User.query.filter_by(name=name).first()

            if user_this_name:
                if user_this_email:
                    already_exists = already_exists + " and "
                already_exists = already_exists + "name"

        if user_this_email or user_this_name:
            raise AlreadyExistsError(f"{already_exists} already exists")


def validate_keys_create_user(data: dict):
    """Raise error case have invalid keys or missing keys when creating the user

    Args:
        data(dict): request data
    """
    required_keys = ["email", "name", "password"]
    received_keys = [key for key in data]

    validate_keys(required_keys, received_keys, required_keys)


def validate_key_login_user(data: dict):
    """Raise error case have invalid keys or missing keys when logging in

    Args:
        data(dict): request data
    """
    required_keys = ["email", "password"]
    received_keys = [key for key in data]

    validate_keys(required_keys, received_keys, required_keys)


def validate_keys_update_user(data: dict):
    """Raise error case have invalid keys when update data user

    Args:
        data(dict): request data
    """
    valid_keys = ["email", "name", "password", "is_adm"]
    received_keys = [key for key in data]

    validate_keys(valid_keys, received_keys)

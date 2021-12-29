from flask import request, current_app, jsonify
from http import HTTPStatus
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user_model import User
from app.utils.user_utils import (
    user_unique_value_already_exists,
    validate_keys_create_user,
    validate_key_login_user,
    validate_keys_update_user,
)

from app.exc.type_exceptions import IncorrectTypeError
from app.exc.key_exeptions import InvalidKeyError
from app.exc.format_exceptions import InvalidFormatError, InvalidStringSizeError
from app.exc.already_exists_exceptions import AlreadyExistsError

import ipdb


def create_user():
    session = current_app.db.session
    data = request.json
    try:
        user_unique_value_already_exists(data)
        validate_keys_create_user(data)
        password_to_hash = data.pop("password")

        new_user: User = User(**data)

        new_user.password = password_to_hash

        session.add(new_user)
        session.commit()

        return jsonify(new_user), HTTPStatus.CREATED
    except IncorrectTypeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidFormatError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except AlreadyExistsError as e:
        return jsonify(e.message), HTTPStatus.CONFLICT
    except InvalidKeyError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidStringSizeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST


def login():
    data = request.json

    try:
        validate_key_login_user(data)

        user_email = data["email"]
        user_password = data["password"]

        found_user: User = User.query.filter_by(email=user_email).first()

        if not found_user:
            return jsonify({"msg": "User not found"}), HTTPStatus.NOT_FOUND

        if found_user.verify_password(user_password):
            access_token = create_access_token(user_email)
            return jsonify({"access_token": access_token}), HTTPStatus.OK
        else:
            return jsonify({"msg": "Unauthorized"}), HTTPStatus.UNAUTHORIZED

    except IncorrectTypeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidFormatError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidKeyError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST


def get_all_users():
    users = User.query.all()

    return jsonify(users), HTTPStatus.OK


def get_by_user(user_id: int):
    user: User = User.query.filter_by(user_id=user_id).first()

    if not user:
        return jsonify({"msg": "User not found"}), HTTPStatus.NOT_FOUND

    return jsonify(user), HTTPStatus.OK


@jwt_required()
def update_user(user_id: int):
    session = current_app.db.session
    user: User = User.query.filter_by(user_id=user_id).first()
    data: dict = request.json

    if not user:
        return jsonify({"msg": "User not found"}), HTTPStatus.NOT_FOUND
    if user.email != get_jwt_identity():
        return jsonify({"msg": "Unauthorized"}), HTTPStatus.UNAUTHORIZED

    try:
        user_unique_value_already_exists(data)
        validate_keys_update_user(data)

        if "password" in data:
            password_to_hash = data.pop("password")
            user.password = password_to_hash

        for key, value in data.items():
            setattr(user, key, value)

        session.commit()

        return {}, HTTPStatus.NO_CONTENT
    except AlreadyExistsError as e:
        return jsonify(e.message), HTTPStatus.CONFLICT
    except IncorrectTypeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidFormatError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidKeyError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidStringSizeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST


# @jwt_required()
# def delete_user(user_id: int):
#     session = current_app.db.session
#     user: User = User.query.filter_by(user_id=user_id).first()

#     if not user:
#         return jsonify({"msg": "User not found"}), HTTPStatus.NOT_FOUND
#     if user.email != get_jwt_identity():
#         return jsonify({"msg": "Unauthorized"}), HTTPStatus.UNAUTHORIZED

#     session.delete(user)
#     session.commit()

#     return {}, HTTPStatus.NO_CONTENT

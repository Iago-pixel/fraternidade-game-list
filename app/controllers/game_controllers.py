from flask import request, current_app, jsonify
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.game_model import Game
from app.models.user_model import User
from app.models.user_game_vote import UserGameVote
from app.utils.game_utils import (
    game_name_already_exists,
    validate_keys_create_game,
    validate_keys_update_game,
    vote_already_exists,
)

from app.exc.key_exeptions import InvalidKeyError
from app.exc.type_exceptions import IncorrectTypeError
from app.exc.format_exceptions import InvalidStringSizeError, InvalidNumberError
from app.exc.already_exists_exceptions import AlreadyExistsError
from sqlalchemy.exc import DataError


@jwt_required()
def create_game():
    session = current_app.db.session
    data = request.json

    user_email = get_jwt_identity()
    current_user: User = User.query.filter_by(email=user_email).first()
    current_user_id = current_user.user_id

    try:
        game_name_already_exists(data)
        validate_keys_create_game(data)
        data["creator_id"] = current_user_id
        new_game: Game = Game(**data)

        session.add(new_game)
        session.commit()

        return jsonify(new_game), HTTPStatus.CREATED
    except IncorrectTypeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidStringSizeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except AlreadyExistsError as e:
        return jsonify(e.message), HTTPStatus.CONFLICT
    except InvalidKeyError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except DataError:
        return (
            jsonify({"msg": "Number of votes exceeds maximum supported by database"}),
            HTTPStatus.BAD_REQUEST,
        )
    except InvalidNumberError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST


def get_all_games():
    games: list = Game.query.all()

    return jsonify(games), HTTPStatus.OK


def get_games_ordered():
    games_ordered: list = Game.query.order_by(Game.votes.desc()).all()

    return jsonify(games_ordered), HTTPStatus.OK


def get_by_game(game_id: int):
    game: Game = Game.query.filter_by(game_id=game_id).first()

    if not game:
        return jsonify({"msg": "Game not found"}), HTTPStatus.NOT_FOUND

    return jsonify(game), HTTPStatus.OK


@jwt_required()
def update_game(game_id: int):
    session = current_app.db.session
    game: Game = Game.query.filter_by(game_id=game_id).first()
    data: dict = request.json

    creator: User = game.creator
    current_user: User = User.query.filter_by(email=get_jwt_identity()).first()

    if not game:
        return jsonify({"msg": "Game not found"}), HTTPStatus.NOT_FOUND
    if not current_user.is_adm and creator.email != current_user.email:
        return jsonify({"msg": "Unauthorized"}), HTTPStatus.UNAUTHORIZED

    try:
        game_name_already_exists(data)
        validate_keys_update_game(data)

        for key, value in data.items():
            setattr(game, key, value)

        session.commit()

        return {}, HTTPStatus.NO_CONTENT
    except IncorrectTypeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidStringSizeError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except InvalidNumberError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST
    except DataError:
        return (
            jsonify({"msg": "Number of votes exceeds maximum supported by database"}),
            HTTPStatus.BAD_REQUEST,
        )
    except AlreadyExistsError as e:
        return jsonify(e.message), HTTPStatus.CONFLICT
    except InvalidKeyError as e:
        return jsonify(e.message), HTTPStatus.BAD_REQUEST


@jwt_required()
def add_vote(game_id: int):
    session = current_app.db.session
    game: Game = Game.query.filter_by(game_id=game_id).first()
    current_user: User = User.query.filter_by(email=get_jwt_identity()).first()

    try:
        vote_already_exists(game_id, current_user)

        if not game:
            return jsonify({"msg": "Game not found"}), HTTPStatus.NOT_FOUND

        setattr(game, "votes", game.votes + 1)

        new_vote: UserGameVote = UserGameVote(game_id=game_id)
        current_user.vote_list.append(new_vote)

        session.commit()

        return {}, HTTPStatus.NO_CONTENT
    except AlreadyExistsError as e:
        return jsonify(e.message), HTTPStatus.CONFLICT


@jwt_required()
def delete_game(game_id: int):
    session = current_app.db.session
    game: Game = Game.query.filter_by(game_id=game_id).first()

    if not game:
        return jsonify({"msg": "Game not found"}), HTTPStatus.NOT_FOUND

    creator: User = game.creator
    current_user: User = User.query.filter_by(email=get_jwt_identity()).first()

    if not current_user.is_adm and creator.email != current_user.email:
        return jsonify({"msg": "Unauthorized"}), HTTPStatus.UNAUTHORIZED

    session.delete(game)
    session.commit()

    return {}, HTTPStatus.NO_CONTENT

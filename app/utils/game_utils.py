from app.models.game_model import Game
from app.models.user_model import User
from app.exc.already_exists_exceptions import AlreadyExistsError
from app.utils.generics_utils import validate_keys


def game_name_already_exists(data: dict):
    """Raise a error if  game name already exists

    Args:
        data(dict): request data
    """
    if "name" in data:
        name = data["name"]
        if isinstance(name, str):
            game_this_name: Game = Game.query.filter_by(name=name).first()
            if game_this_name:
                raise AlreadyExistsError("name already exists")


def validate_keys_create_game(data: dict):
    """Raise error case have invalid keys or missing keys when creating the game

    Args:
        data(dict): resquest data
    """
    required_keys = ["name", "description", "votes"]
    received_keys = [key for key in data]

    validate_keys(required_keys, received_keys, required_keys)


def validate_keys_update_game(data):
    """Raise error case have invalid keys when creating the game

    Args:
        data(dict): resquest data
    """
    valid_keys = ["name", "description", "votes"]
    received_keys = [key for key in data]

    validate_keys(valid_keys, received_keys)


def vote_already_exists(game_id: int, current_user: User):
    """Raise error case vote already exists

    Args:
        game_id(int): game id being voted
        current_user(User): logged in user
    """
    for user_game_vote in current_user.vote_list:
        if user_game_vote.game_id == game_id:
            raise AlreadyExistsError("Current user has already voted for this game")

from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    from app.models.user_model import User
    from app.models.game_model import Game
    from app.models.user_game_vote import UserGameVote

    Migrate(app, app.db)

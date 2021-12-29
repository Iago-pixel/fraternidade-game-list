from flask import Flask
from app.routes.user_blueprint import bp as bp_user
from app.routes.game_blueprint import bp as bp_game


def init_app(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_game)

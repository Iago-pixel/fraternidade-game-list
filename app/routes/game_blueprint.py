from flask import Blueprint
from app.controllers.game_controllers import (
    create_game,
    get_all_games,
    get_games_ordered,
    get_by_game,
    update_game,
    add_vote,
    delete_game,
)

bp = Blueprint("bp_game", __name__, url_prefix="/games")

bp.post("")(create_game)
bp.get("")(get_all_games)
bp.get("/ordered")(get_games_ordered)
bp.get("/<int:game_id>")(get_by_game)
bp.patch("/<int:game_id>")(update_game)
bp.patch("/<int:game_id>/vote")(add_vote)
bp.delete("/<int:game_id>")(delete_game)

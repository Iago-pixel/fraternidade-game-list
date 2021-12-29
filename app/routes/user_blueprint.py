from flask import Blueprint
from app.controllers.user_controllers import (
    create_user,
    login,
    get_all_users,
    get_by_user,
    update_user,
)

bp = Blueprint("bp_user", __name__, url_prefix="/users")

bp.post("")(create_user)
bp.post("/login")(login)
bp.get("")(get_all_users)
bp.get("/<int:user_id>")(get_by_user)
bp.patch("/<int:user_id>")(update_user)
# bp.delete("/<int:user_id>")(delete_user)

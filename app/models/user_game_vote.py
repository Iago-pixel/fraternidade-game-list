from app.configs.database import db
from dataclasses import dataclass


@dataclass
class UserGameVote(db.Model):
    user_game_vote_id: int
    user_id: int
    game_id: int

    __tablename__ = "user_game_votes"

    user_game_vote_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("games.game_id"), nullable=False)

from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, validates
from app.utils.generics_utils import validate_type, validate_string_size

from app.exc.format_exceptions import InvalidNumberError


@dataclass
class Game(db.Model):
    game_id: int
    name: str
    description: str
    votes: int
    creator_id: int

    __tablename__ = "games"

    game_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))
    votes = db.Column(db.Integer, default=0)
    creator_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    creator = relationship("User")

    vote_list = relationship("UserGameVote", cascade="all, delete-orphan")

    @validates("name")
    def validate_name(self, key, name):
        validate_type(key, name, str)
        validate_string_size(key, name, 80)

        return name

    @validates("description")
    def validade_description(self, key, description):
        if description != None:
            validate_type(key, description, str)
            validate_string_size(key, description, 255)

        return description

    @validates("votes")
    def validate_votes(self, key, votes):
        if votes != None:
            validate_type(key, votes, int)
            if votes < 0:
                raise InvalidNumberError("Votes cannot be a negative number")

        return votes

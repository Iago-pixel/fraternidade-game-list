from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, validates
import re
from app.utils.generics_utils import validate_type, validate_string_size

from app.exc.format_exceptions import InvalidFormatError


@dataclass
class User(db.Model):
    user_id: int
    email: str
    name: str
    is_adm: bool

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(255))
    is_adm = db.Column(db.Boolean, default=False)

    vote_list = relationship("UserGameVote")

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        validate_type("password", password_to_hash, str)
        if not re.fullmatch(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@$#%&çÇ`\'^~*]).{8,}$",
            password_to_hash,
        ):
            raise InvalidFormatError(
                "The password must contain at least 8 characters, 1 lowercase letter, 1 uppercase letter, 1 number and 1 special character"
            )

        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    @validates("email")
    def validate_email(self, key, email):
        validate_type(key, email, str)

        if not re.fullmatch(
            r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{2,3}$", email
        ):
            raise InvalidFormatError("Incorrect email format")

        return email

    @validates("name")
    def validate_name(self, key, name):
        validate_type(key, name, str)
        validate_string_size(key, name, 80)

        return name

    @validates("is_adm")
    def validate_is_adm(self, key, is_adm):
        validate_type(key, is_adm, bool)

        return is_adm

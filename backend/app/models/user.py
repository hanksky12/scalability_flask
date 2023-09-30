from werkzeug.security import check_password_hash
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import AbstractBase

class User(AbstractBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

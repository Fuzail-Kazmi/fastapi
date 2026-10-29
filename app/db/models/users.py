from typing import Optional
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.core.database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, nullable=False, unique=True)

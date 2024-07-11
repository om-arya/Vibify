from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email_address = Column(String)

    vibes = relationship("Vibe", back_populates="owner")


class Vibe(Base):
    __tablename__ = "vibes"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="vibes")
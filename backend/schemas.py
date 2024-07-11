from pydantic import BaseModel

class VibeBase(BaseModel):
    title: str

class VibeCreate(VibeBase):
    pass

class Vibe(VibeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    username: str
    vibes: list[Vibe] = []

    class Config:
        orm_mode = True
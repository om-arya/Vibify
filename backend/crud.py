from sqlalchemy.orm import Session

from . import models, schemas

# CREATE USERS

"""
Save a new user into the database.
"""
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, password=user.password)
    
    db.add(db_user)

    db.commit()
    db.refresh(db_user)
    return db_user

# GET USERS

"""
Get the user from the database with the specified username.
"""
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

"""
Get the user from the database with the specified email address.
"""
def get_user_by_email_address(db: Session, email_address: str):
    return db.query(models.User).filter(models.User.email_address == email_address).first()

# CREATE VIBES

"""
Save a new vibe into the database, belonging to the user with the
specified username.
"""
def create_user_vibe(db: Session, vibe: schemas.VibeCreate, username: str):
    db_vibe = models.Vibe(**vibe.dict(), owner_id=username)

    db.add(db_vibe)

    db.commit()
    db.refresh(db_vibe)
    return db_vibe
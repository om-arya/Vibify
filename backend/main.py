from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE USERS

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user_by_username = crud.get_user_by_username(db, username=user.username)
    if db_user_by_username:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    db_user_by_email_address = crud.get_user_by_email(db, email=user.email)
    if db_user_by_email_address:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)

# GET USERS

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user_by_username(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    
    return db_user

# CREATE VIBES

@app.post("/users/{user_id}/vibes/", response_model=schemas.Vibe)
def create_vibe_for_user(username: str, vibe: schemas.VibeCreate, db: Session = Depends(get_db)):
    return crud.create_user_vibe(db=db, vibe=vibe, user_id=username)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.schemas.user_schema import UserCreate
from app.services.user_service import create_user, get_users

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users")
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.email)


@router.get("/users")
def get_users_api(db: Session = Depends(get_db)):
    return get_users(db)
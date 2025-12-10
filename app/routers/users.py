from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, auth, database
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Fake current user (for now, until we implement real JWT)
def get_current_user(db: Session = Depends(get_db)):
    return db.query(models.User).first()  # always returns the first user

@router.put("/update", response_model=schemas.UserOut)
def update_profile(user_update: schemas.UserUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if user_update.username:
        current_user.username = user_update.username
    if user_update.email:
        current_user.email = user_update.email

    db.commit()
    db.refresh(current_user)
    return current_user

@router.put("/change-password")
def change_password(data: schemas.UserPasswordChange, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if not auth.verify_password(data.old_password, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect current password")

    current_user.hashed_password = auth.hash_password(data.new_password)
    db.commit()
    return {"message": "Password updated successfully"}

from fastapi import status, HTTPException
from ..hashing import get_password_hash
from sqlalchemy.orm import Session
from .. import models


def create(request, db: Session):
    hashed_password = get_password_hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    users = db.query(models.User).all()
    return users


def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found with the ID {id}')
    return user
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas, security
from ..dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=List[schemas.UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schemas.UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=schemas.UserSchema)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this user")
    return crud.update_user(db=db, user_id=user_id, user=user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this user")
    crud.delete_user(db=db, user_id=user_id)
    return {"ok": True}

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: security.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = security.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=security.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {"access_token": access_token, "token_type": "bearer"}
```
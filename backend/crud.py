from sqlalchemy.orm import Session
from . import models, schemas
from .security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_surveys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Survey).offset(skip).limit(limit).all()


def create_user_survey(db: Session, survey: schemas.SurveyCreate, user_id: int):
    db_survey = models.Survey(**survey.dict(), owner_id=user_id)
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey


def get_responses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Response).offset(skip).limit(limit).all()


def create_survey_response(db: Session, response: schemas.ResponseCreate, survey_id: int):
    db_response = models.Response(**response.dict(), survey_id=survey_id)
    db.add(db_response)
    db.commit()
    db.refresh(db_response)
    return db_response


def get_survey_by_id(db: Session, survey_id: int):
    return db.query(models.Survey).filter(models.Survey.id == survey_id).first()


def get_survey_responses(db: Session, survey_id: int):
    return db.query(models.Response).filter(models.Response.survey_id == survey_id).all()


def get_user_surveys(db: Session, user_id: int):
    return db.query(models.Survey).filter(models.Survey.owner_id == user_id).all()


def delete_survey(db: Session, survey_id: int):
    db.query(models.Survey).filter(models.Survey.id == survey_id).delete()
    db.commit()


def update_survey(db: Session, survey_id: int, survey: schemas.SurveyUpdate):
    db.query(models.Survey).filter(models.Survey.id == survey_id).update(survey.dict())
    db.commit()
    return get_survey_by_id(db, survey_id=survey_id)


def delete_response(db: Session, response_id: int):
    db.query(models.Response).filter(models.Response.id == response_id).delete()
    db.commit()


def update_response(db: Session, response_id: int, response: schemas.ResponseUpdate):
    db.query(models.Response).filter(models.Response.id == response_id).update(response.dict())
    db.commit()
    return db.query(models.Response).filter(models.Response.id == response_id).first()
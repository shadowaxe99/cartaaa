from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..dependencies import get_db, get_current_user
from ..security import get_password_hash

router = APIRouter(
    prefix="/api/surveys",
    tags=["surveys"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Survey)
def create_survey(
    survey: schemas.SurveyCreate, db: Session = Depends(get_db)
):
    db_survey = crud.get_survey_by_title(db, title=survey.title)
    if db_survey:
        raise HTTPException(status_code=400, detail="Survey already registered")
    return crud.create_survey(db=db, survey=survey)

@router.get("/", response_model=List[schemas.Survey])
def read_surveys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    surveys = crud.get_surveys(db, skip=skip, limit=limit)
    return surveys

@router.get("/{survey_id}", response_model=schemas.Survey)
def read_survey(survey_id: int, db: Session = Depends(get_db)):
    db_survey = crud.get_survey(db, survey_id=survey_id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return db_survey

@router.put("/{survey_id}", response_model=schemas.Survey)
def update_survey(
    survey_id: int, survey: schemas.SurveyUpdate, db: Session = Depends(get_db)
):
    db_survey = crud.get_survey(db, survey_id=survey_id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return crud.update_survey(db=db, survey=survey, survey_id=survey_id)

@router.delete("/{survey_id}", response_model=schemas.Survey)
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    db_survey = crud.get_survey(db, survey_id=survey_id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return crud.delete_survey(db=db, survey_id=survey_id)

@router.post("/{survey_id}/responses/", response_model=schemas.Response)
def create_survey_response(
    survey_id: int, response: schemas.ResponseCreate, db: Session = Depends(get_db)
):
    return crud.create_survey_response(db=db, response=response, survey_id=survey_id)

@router.get("/{survey_id}/responses/", response_model=List[schemas.Response])
def read_survey_responses(survey_id: int, db: Session = Depends(get_db)):
    responses = crud.get_responses_for_survey(db, survey_id=survey_id)
    if responses is None:
        raise HTTPException(status_code=404, detail="Responses not found")
    return responses

@router.get("/{survey_id}/analytics/", response_model=schemas.Analytics)
def get_survey_analytics(survey_id: int, db: Session = Depends(get_db)):
    survey = crud.get_survey(db, survey_id=survey_id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    responses = crud.get_responses_for_survey(db, survey_id=survey_id)
    return crud.analyze_responses(responses)
from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional, Union
from datetime import datetime

# Define the structure for user data
class UserSchema(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    hashed_password: str
    is_active: Optional[bool] = True
    surveys: List[int] = []

    class Config:
        orm_mode = True

# Define the structure for survey questions
class QuestionSchema(BaseModel):
    id: Optional[int] = None
    survey_id: int
    text: str
    response_type: constr(regex='^(multiple choice|open-ended)$')
    options: Optional[List[str]] = None

    class Config:
        orm_mode = True

# Define the structure for survey responses
class ResponseSchema(BaseModel):
    id: Optional[int] = None
    question_id: int
    user_id: int
    response: Union[str, List[str]]

    class Config:
        orm_mode = True

# Define the structure for survey data
class SurveySchema(BaseModel):
    id: Optional[int] = None
    creator_id: int
    title: str
    description: Optional[str] = None
    language: str
    expiration_date: Optional[datetime] = None
    max_responses: Optional[int] = None
    questions: List[QuestionSchema]
    responses: List[ResponseSchema] = []

    class Config:
        orm_mode = True

# Define the structure for analytics data
class AnalyticsSchema(BaseModel):
    survey_id: int
    sentiment_analysis: Optional[dict] = {}
    keyword_extraction: Optional[dict] = {}
    response_statistics: Optional[dict] = {}

    class Config:
        orm_mode = True

# Define the structure for login payload
class LoginSchema(BaseModel):
    email: EmailStr
    password: str

# Define the structure for registration payload
class RegisterSchema(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

# Define the structure for survey creation payload
class SurveyCreateSchema(BaseModel):
    title: str
    description: Optional[str] = None
    language: str
    expiration_date: Optional[datetime] = None
    max_responses: Optional[int] = None
    questions: List[QuestionSchema]

# Define the structure for survey update payload
class SurveyUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    expiration_date: Optional[datetime] = None
    max_responses: Optional[int] = None
    questions: Optional[List[QuestionSchema]] = None

# Define the structure for response submission payload
class ResponseSubmitSchema(BaseModel):
    question_id: int
    response: Union[str, List[str]]
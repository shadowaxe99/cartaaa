```python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# Association table for many-to-many relationship between Survey and User
survey_responses = Table(
    'survey_responses',
    Base.metadata,
    Column('survey_id', ForeignKey('surveys.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    surveys = relationship('Survey', secondary=survey_responses, back_populates='respondents')

class Survey(Base):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    creator_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='created_surveys')
    questions = relationship('Question', back_populates='survey')
    responses = relationship('Response', back_populates='survey')
    respondents = relationship('User', secondary=survey_responses, back_populates='surveys')
    created_at = Column(DateTime, default=func.now())
    expires_at = Column(DateTime)

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    question_type = Column(String)  # e.g., 'multiple_choice', 'open_ended'
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    survey = relationship('Survey', back_populates='questions')
    options = relationship('Option', back_populates='question')

class Option(Base):
    __tablename__ = 'options'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship('Question', back_populates='options')

class Response(Base):
    __tablename__ = 'responses'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_text = Column(Text)
    user = relationship('User')
    survey = relationship('Survey', back_populates='responses')
    question = relationship('Question')
    created_at = Column(DateTime, default=func.now())

# Additional models for analytics and integrations can be added here following the same pattern.
```
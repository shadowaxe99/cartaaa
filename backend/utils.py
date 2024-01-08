```python
import re
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

# Shared dependencies and variables
from .config import settings

# Cryptographic context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")

def verify_password(plain_password, hashed_password):
    """
    Verifies a password against a hashed version.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    Generates a hashed version of a password.
    """
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a new access token with the given data and expiry.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def validate_email(email: str) -> bool:
    """
    Validates the format of an email address.
    """
    return re.match(EMAIL_REGEX, email) is not None

def generate_survey_link(survey_id: str, user_id: str) -> str:
    """
    Generates a unique survey link for a user.
    """
    token_data = {"survey_id": survey_id, "user_id": user_id}
    token = create_access_token(data=token_data, expires_delta=timedelta(hours=24))
    survey_link = f"{settings.SURVEY_BASE_URL}/take-survey?token={token}"
    return survey_link

def decode_survey_token(token: str) -> dict:
    """
    Decodes a survey token to retrieve the survey_id and user_id.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload if "survey_id" in payload and "user_id" in payload else None
    except jwt.JWTError:
        return None
```
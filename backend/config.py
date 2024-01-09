```python
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///./sql_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # Carta integration configuration
    CARTA_API_KEY = os.getenv('CARTA_API_KEY')

    # CRM integration configuration
    CRM_API_KEY = os.getenv('CRM_API_KEY')

    # Security configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # Email configuration for survey distribution
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() in ('true', '1', 't')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your-email@example.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your-email-password')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'no-reply@example.com')

    # Application configuration
    APP_NAME = 'Olvy Cap Table Management'
    APP_VERSION = '1.0.0'

# Configuration for development environment
class DevelopmentConfig(Config):
    DEBUG = True

# Configuration for testing environment
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./test_database.db'

# Configuration for production environment
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

# Export configurations for use in the application
config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
```
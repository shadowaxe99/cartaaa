```python
from flask import Flask
from flask_cors import CORS
from .database import engine, Base
from .routers import survey, user, auth
from .dependencies import get_db
from .config import settings

# Create the Flask application
app = Flask(__name__)
CORS(app)

# Database initialization
Base.metadata.create_all(bind=engine)

# Dependency injection
app.dependency_overrides[get_db] = get_db

# Register blueprints (routers)
app.register_blueprint(user.router, url_prefix='/api/users')
app.register_blueprint(survey.router, url_prefix='/api/surveys')
app.register_blueprint(auth.router, url_prefix='/api/auth')

# Run the application
if __name__ == "__main__":
    app.run(host=settings.server_host, port=settings.server_port)
```
```python
from flask import Flask
from backend.config import Config
from backend.database import db_session, init_db
from backend.routers import survey, user, auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    init_db()

    # Register blueprints
    app.register_blueprint(survey.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(auth.bp)

    # Teardown context
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
```
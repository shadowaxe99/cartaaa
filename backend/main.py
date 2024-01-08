```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import survey, user, auth
from .database import engine
from . import models

# Create all tables in the database
# Comment this out if you're using Alembic migrations
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS middleware
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(survey.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Olvy's Cap Table Management and Customer Survey Tool API"}

# Add more endpoints here if needed
```
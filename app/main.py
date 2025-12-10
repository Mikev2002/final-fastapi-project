from fastapi import FastAPI
from app import models, database
from app.routers import auth, users

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API is working!"}

from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="LegalEase API",
    description="AI-powered legal document generator",
    version="1.0.0",
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "LegalEase API is running"}

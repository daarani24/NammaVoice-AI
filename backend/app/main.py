from fastapi import FastAPI
from app.api import auth_router

app=FastAPI(title="NammaVoice AI")

app.include_router(auth_router.router)

@app.get("/")
def root():
    return {"message":"NammaVoice AI API running"}
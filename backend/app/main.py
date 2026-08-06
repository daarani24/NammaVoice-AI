from fastapi import FastAPI

app=FastAPI(title="NammaVoice AI")

@app.get("/")
def root():
    return {"message":"NammaVoice AI API running"}
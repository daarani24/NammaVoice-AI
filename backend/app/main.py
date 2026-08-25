from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth_router, complaint_router, officer_router, reference_router, collector_router, admin_router
from app.api.deps import get_current_user 

app = FastAPI(title="NammaVoice AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(complaint_router.router)
app.include_router(officer_router.router)
app.include_router(reference_router.router)
app.include_router(collector_router.router)
app.include_router(admin_router.router)

@app.get("/")
def root():
    return {"message": "NammaVoice AI API running"}

@app.get("/me")
def read_me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role
    }
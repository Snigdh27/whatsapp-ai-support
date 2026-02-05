from fastapi import FastAPI
from app.api.webhook import router as webhook_router

app = FastAPI(title="Whatsapp AI Support")

app.include_router(webhook_router,prefix="/whatsapp")

@app.get("/")
def health_check():
    return {"status":"Backend running successfully!"}
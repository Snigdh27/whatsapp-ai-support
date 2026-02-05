from fastapi import FastAPI

app = FastAPI(title="Whatsapp AI Support")

@app.get("/")
def health_check():
    return {"status":"Backend running successfully!"}
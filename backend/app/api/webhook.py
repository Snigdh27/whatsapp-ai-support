from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/webhook")
async def verify():
    return {"status":"Webhook verification endpoint"}

@router.post("/webhook")
async def receive_message(request:Request):
    payload = await request.json()
    print(payload)
    return {"status":"Message received"}
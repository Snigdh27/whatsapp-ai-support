from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import PlainTextResponse
import os
import json
from dotenv import load_dotenv
from app.services.ai_agent import generate_reply

load_dotenv()

router = APIRouter()
VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN")

@router.get("/webhook")
async def verify(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    print("Verification hit")
    print("Mode:", mode)
    print("Token received:", token)
    print("Expected token:", VERIFY_TOKEN)

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    raise HTTPException(status_code=403)


@router.post("/webhook")
async def receive_message(request:Request):
    payload = await request.json()
    print(payload)
    try:
        if payload.get("object") == "whatsapp_business_account":
            entry = payload["entry"][0]
            change = entry["changes"][0]
            value = change["value"]

            if "messages" in value:
                message = value["messages"][0]
                sender = message["from"]
                text = message["text"]["body"]

                print("Sender:", sender)
                print("Message:", text)
                reply = generate_reply(text)
                from app.services.whatsapp_service import send_message
                send_message(sender, reply)

            else:
                print("No messages field found")

        else:
            print("Not a WhatsApp message event")

    except Exception as e:
        print("Error parsing webhook:", str(e))

    return {"status": "ok"}
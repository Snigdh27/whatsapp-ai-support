import requests
from dotenv import load_dotenv
import os

def send_message(to,text):
    url=f"https://graph.facebook.com/v22.0/{os.getenv('WHATSAPP_PHONE_ID')}/messages"
    headers = {
        "Authorization":f"Bearer {os.getenv('WHATSAPP_TOKEN')}",
        "Content-Type":"application/json"
    }

    payload = {
        "messaging_product":"whatsapp",
        "to":to,
        "type":"text",
        "text":{
            "body":text
        }
    }

    print("Send message response:")
    response = requests.post(url,headers=headers,json=payload)
    print(response.status_code)
    print(response.text)
from twilio.rest import Client
import json
import os
from dotenv import load_dotenv

load_dotenv(".env")

TWILIO_PHONE = os.getenv("TWILIO_PHONE")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")


def sendTwilioSms(to_number, body):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(body=body, from_=TWILIO_PHONE, to=to_number)
    print(message.sid, to_number, body)
    return message.sid


def sendLocation(location: str):
    with open(os.path.join("db", "contacts.json"), "r") as f:
        data = json.load(f)

        authorityPhones = data["authorities"]
        trustedPhones = data["trusted"]

        for phone in authorityPhones:
            try:
                sendTwilioSms(phone, location)
            except Exception as _:
                pass

        for phone in trustedPhones:
            try:
                sendTwilioSms(phone, location)
            except Exception as _:
                pass

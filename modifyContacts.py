import json
import os

CONTACTS_FILE = os.path.join("db", "contacts.json")


def addContact(phone: str) -> None:
    if not phone.startswith("+91"):
        phone = "+91" + phone

    with open(CONTACTS_FILE, "r") as f:
        data = json.load(f)

    if phone not in data.get("trusted", []):
        data["trusted"].append(phone)

    with open(CONTACTS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def removeContact(phone: str) -> None:
    if not phone.startswith("+91"):
        phone = "+91" + phone

    with open(CONTACTS_FILE, "r") as f:
        data = json.load(f)

    if phone in data.get("trusted", []):
        data["trusted"].remove(phone)

    with open(CONTACTS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def purgeContacts() -> None:
    with open(CONTACTS_FILE, "r") as f:
        data = json.load(f)

    data["trusted"].clear()

    with open(CONTACTS_FILE, "w") as f:
        json.dump(data, f, indent=4)


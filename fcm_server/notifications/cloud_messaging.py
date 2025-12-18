import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred)


def send_fcm_message(registration_tokens: str, data: dict):
    message = messaging.MulticastMessage(
        data=data,
        tokens=registration_tokens
    )

    response = messaging.send_each_for_multicast(message)
    return response

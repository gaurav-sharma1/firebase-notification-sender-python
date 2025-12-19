import firebase_admin
from firebase_admin import credentials, messaging
from .models import FCMToken

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred)


def send_notification_to_user(user_id, data):

    tokens = list(
        FCMToken.objects
        .filter(user_id=user_id)
        .values_list('token', flat=True)
    )

    if not tokens:
        raise Exception("No tokens found for user")

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=data['title'],
            body=data['message'],
        ),
        data=data,
        tokens=tokens
    )

    response = messaging.send_each_for_multicast(message)
    return response

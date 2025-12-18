from django.urls import path
from .views import SendFCMMessageAPIView

urlpatterns = [
    path('send/', SendFCMMessageAPIView.as_view(), name='send-fcm'),
]

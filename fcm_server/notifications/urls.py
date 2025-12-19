from django.urls import path
from .views import SendNotificationByUserAPIView, GetRegisteredUsersAPIView
from .views import RegisterUserTokenAPIView

urlpatterns = [
    path('register/', RegisterUserTokenAPIView.as_view()),
    path('users/', GetRegisteredUsersAPIView.as_view()),
    path('sendUser', SendNotificationByUserAPIView.as_view()),
]

from django.urls import path

from notifications.views import RegisterUserAPIView, GetUsersAPIView, SendNotificationByUserAPIView
from notifications.views.user_views import DeleteUserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('users/', GetUsersAPIView.as_view()),
    path('users/<uuid:user_id>/', DeleteUserAPIView.as_view()),
    path('send', SendNotificationByUserAPIView.as_view()),
]

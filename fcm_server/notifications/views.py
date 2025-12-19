from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import AppUser, FCMToken
from .serializers import RegisterUserTokenSerializer, SendUserNotificationSerializer, AppUserResponseSerializer, \
    AppUserWithTokensSerializer
from .cloud_messaging import send_notification_to_user

class RegisterUserTokenAPIView(APIView):

    def post(self, request):
        serializer = RegisterUserTokenSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        token = serializer.validated_data['registration_token']

        # Get or create user
        user, created = AppUser.objects.get_or_create(username=username)

        # Prevent duplicate token
        FCMToken.objects.get_or_create(
            user=user,
            token=token
        )

        return Response(
            {
                "user_id": user.id,
                "username": user.username
            },
            status=status.HTTP_201_CREATED
        )

class UserTokenAPIView(APIView):

    def get(self, request):
        serializer = RegisterUserTokenSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        token = serializer.validated_data['registration_token']

        # Get or create user
        user, created = AppUser.objects.get_or_create(username=username)

        # Prevent duplicate token
        FCMToken.objects.get_or_create(
            user=user,
            token=token
        )

        return Response(
            {
                "user_id": user.id,
                "username": user.username
            },
            status=status.HTTP_201_CREATED
        )

class SendNotificationByUserAPIView(APIView):

    def post(self, request):
        serializer = SendUserNotificationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        user_id = serializer.validated_data['user_id']
        data = serializer.validated_data['data']

        response = send_notification_to_user(user_id, data)

        return Response(
            {
                "success": response.success_count,
                "failure": response.failure_count
            }
        )

class GetRegisteredUsersAPIView(APIView):

    def get(self, request):
        users = AppUser.objects.all()
        serializer = AppUserWithTokensSerializer(users, many=True)
        return Response(serializer.data)
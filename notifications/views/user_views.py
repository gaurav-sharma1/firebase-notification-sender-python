from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from notifications.models import AppUser
from notifications.serializers import RegisterUserTokenSerializer
from notifications.serializers.user_serializers import UserResponseSerializer, AppUserWithTokensSerializer
from notifications.services.user_service import UserService


class RegisterUserAPIView(APIView):

    def post(self, request):
        serializer = RegisterUserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserService.register_user_token(
            serializer.validated_data['username'],
            serializer.validated_data['registration_token']
        )

        return Response(
            UserResponseSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class GetUsersAPIView(APIView):

    def get(self, request):
        users = AppUser.objects.all()
        serializer = AppUserWithTokensSerializer(users, many=True)
        return Response(serializer.data)

class DeleteUserAPIView(APIView):

    def delete(self, request, user_id):
        deleted = UserService.delete_user(user_id)

        if not deleted:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {"message": "User and tokens deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
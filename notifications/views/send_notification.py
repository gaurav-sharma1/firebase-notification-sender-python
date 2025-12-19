from rest_framework.response import Response
from rest_framework.views import APIView

from notifications.serializers.notification_serializers import SendUserNotificationSerializer
from notifications.services.fcm_service import send_notification_to_user


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
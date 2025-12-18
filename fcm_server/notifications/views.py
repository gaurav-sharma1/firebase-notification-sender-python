from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import FCMMessageSerializer
from .cloud_messaging import send_fcm_message


class SendFCMMessageAPIView(APIView):

    def post(self, request):
        serializer = FCMMessageSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        registration_tokens = serializer.validated_data['registration_tokens']
        data = serializer.validated_data['data']

        try:
            response = send_fcm_message(registration_tokens, data)
            return Response(
                {
                    "success_count": response.success_count,
                    "failure_count": response.failure_count
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

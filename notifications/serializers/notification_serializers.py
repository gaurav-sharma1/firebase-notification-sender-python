from rest_framework import serializers

class SendUserNotificationSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    data = serializers.DictField(
        child=serializers.CharField()
    )
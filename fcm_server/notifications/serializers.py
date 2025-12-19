from rest_framework import serializers
from .models import AppUser, FCMToken

class RegisterUserTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    registration_token = serializers.CharField()

class SendUserNotificationSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    data = serializers.DictField(
        child=serializers.CharField()
    )

class AppUserWithTokensSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source='id')
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = AppUser
        fields = ['user_id', 'username', 'tokens']

    def get_tokens(self, obj):
        return list(obj.fcm_tokens.values_list('token', flat=True))

class AppUserResponseSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source='id')

    class Meta:
        model = AppUser
        fields = ['user_id', 'username']
from rest_framework import serializers

class FCMMessageSerializer(serializers.Serializer):
    registration_tokens = serializers.ListField(
        child=serializers.CharField()
    )
    data = serializers.DictField(
        child=serializers.CharField()
    )

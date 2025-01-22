from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
  message = serializers.CharField(max_length=1000)
  user_id = serializers.CharField()

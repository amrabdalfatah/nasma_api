from rest_framework import serializers

from .models import MessageExplainer
from .utils import send_message_to_api

class MessageExplainerSerializer(serializers.ModelSerializer):
  class Meta:
    model = MessageExplainer
    fields = ("id", "_input", "_output")
    extra_kwargs = {
      "_output": {"read_only": True}
    }

  def create(self, validated_data):
    me = MessageExplainer(**validated_data)
    _output = send_message_to_api(validated_data["_input"])
    me._output = _output
    me.save()
    return me
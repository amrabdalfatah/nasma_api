from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatMessageSerializer
from .chatbot_logic import get_response
# from chatbot.chatbot_logic import chatbot_response

class ChatbotView(APIView):
  def post(self, request):
      serializer = ChatMessageSerializer(data=request.data)
      if serializer.is_valid():
          user_message = serializer.validated_data["message"]
          user_id = serializer.validated_data["user_id"]
          bot_reply = get_response(user_message, user_id)
          return Response({"reply": bot_reply}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import serializers

from .models import QustionsTest, PSSTest, PSSResult
 
class QustionsTestSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "content",
      "answer_zero",
      "answer_one",
      "answer_two",
      "answer_three",
      "answer_four",
    )
    model = QustionsTest

class PSSTestSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "title",
      "description",
    )
    model = PSSTest

class PSSResultSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "user_id",
      "test_id",
      "score",
      "test_date",
      "level",
    )
    model = PSSResult
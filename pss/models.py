from django.conf import settings
from django.db import models

  
# Create your models here. 
class PSSTest(models.Model):
  # test_id
  title = models.CharField(max_length=10)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.title
  
class QustionsTest(models.Model):
  content = models.CharField(max_length=400)
  answer_zero = models.CharField(max_length=40, default="Never")
  answer_one = models.CharField(max_length=40, default="Almost Never")
  answer_two = models.CharField(max_length=40, default="Sometimes")
  answer_three = models.CharField(max_length=40, default="Fairly Often")
  answer_four = models.CharField(max_length=40, default="Very Often")

  def __str__(self):
    return self.content
  

class PSSResult(models.Model):
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  test_id = models.ForeignKey(PSSTest, on_delete=models.CASCADE)
  score = models.IntegerField()
  test_date = models.DateTimeField(auto_now_add=True)
  level = models.CharField(max_length=10)
  
  def __str__(self):
    return self.level
from django.urls import path

from .views import QuestionsList, QuestionDetail, PSSResultList, PSSTestDetail

urlpatterns = [
  path("question/<int:pk>/", QuestionDetail.as_view(), name="question_detail"),
  path("questions/", QuestionsList.as_view(), name="questions_list"),
  path("pssresults/", PSSResultList.as_view(), name="pss_result_list"),
  path("psstest/", PSSTestDetail.as_view(), name="pss_test"),
]
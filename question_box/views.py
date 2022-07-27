from rest_framework import generics
from question_box.models import Question
from .serializers import QuestionSerializer


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

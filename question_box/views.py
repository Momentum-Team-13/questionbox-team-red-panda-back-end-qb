from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from question_box.models import Question
from .serializers import QuestionSerializer


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

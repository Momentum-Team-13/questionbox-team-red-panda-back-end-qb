from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from question_box.models import Question, Answer, Game
from .serializers import QuestionSerializer, AnswerSerializer, GameSerializer, CategorySerializer


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class AnswerListView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs.get("pk"))
        serializer.save(user=self.request.user, question=question)


class GamesListView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class CategoryListView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class QuestionByGameView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'game_pk'

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from question_box.models import Category, Question, Answer, Game, Category
from .serializers import QuestionSerializer, AnswerSerializer, GameSerializer, CategorySerializer


class QuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(game_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        game = get_object_or_404(Game, pk=self.kwargs.get("pk"))
        serializer.save(user=self.request.user, game=game)


    # def get_queryset(self):
    #     queryset = Question.objects.all()
    #     search_term = self.request.query_params
    #     if search_term is not None:
    #         pass
    #     return queryset


class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class AnswerListView(generics.ListCreateAPIView):
    # queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs.get("pk"))
        serializer.save(user=self.request.user, question=question)


class GamesListView(generics.ListCreateAPIView):
    # queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(category_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        category = get_object_or_404(Category, pk=self.kwargs.get("pk"))
        serializer.save(category=category)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CreateGameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

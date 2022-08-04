from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from question_box.models import Category, Question, Answer, Game, User
from question_box.permissions import IsOwner
from .serializers import QuestionSerializer, CreateAnswerSerializer, GameSerializer, CategorySerializer, ViewAnswerSerializer


class QuestionListView(generics.ListCreateAPIView):
    # queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticated]

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
    # permission_classes = [IsAuthenticated]


class AnswerListView(generics.ListCreateAPIView):
    # queryset = Answer.objects.all()
    serializer_class = CreateAnswerSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs.get("pk"))
        serializer.save(user=self.request.user, question=question)


class GamesListView(generics.ListCreateAPIView):
    # queryset = Game.objects.all()
    serializer_class = GameSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Game.objects.filter(category_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        category = get_object_or_404(Category, pk=self.kwargs.get("pk"))
        serializer.save(category=category)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]


class CreateGameView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class AddQuestionListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class UserQuestionListView(generics.ListAPIView):

    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(user_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        serializer.save(user=user)


class UserAnswerListView(generics.ListAPIView):

    serializer_class = ViewAnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(user_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.kwargs.get("pk"))
        serializer.save(user=user)


class QuestionDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class AnswerDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = CreateAnswerSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class CategoryDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CreateOrRemoveFavoriteQuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        user = self.request.user
        question = get_object_or_404(Question, pk=self.kwargs['question_pk'])
        user.favorite_questions.add(question)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        question = get_object_or_404(Question, pk=self.kwargs['question_pk'])
        user.favorite_questions.remove(question)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data, status=204)


class CreateOrRemoveFavoriteAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        user = self.request.user
        answer = get_object_or_404(Answer, pk=self.kwargs['answer_pk'])
        user.favorite_answers.add(answer)
        serializer = CreateAnswerSerializer(answer, context={'request': request})
        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        answer = get_object_or_404(Answer, pk=self.kwargs['answer_pk'])
        user.favorite_answers.remove(answer)
        serializer = CreateAnswerSerializer(answer, context={'request': request})
        return Response(serializer.data, status=204)


class UserFavoriteQuestionsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.request.user.favorite_questions.all()


class UserFavoriteAnswersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateAnswerSerializer

    def get_queryset(self):
        return self.request.user.favorite_answers.all()

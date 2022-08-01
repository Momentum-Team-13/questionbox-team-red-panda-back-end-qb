from rest_framework import serializers
from question_box.models import Category, Question, User, Answer, Game


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    favorited_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")
    game = serializers.SlugRelatedField(slug_field="game", read_only=True)

    class Meta:
        model = Question
        fields = ('pk', 'user', 'title', 'description', 'favorited_by', 'game')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    favorited_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")
    question = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'user', 'description', 'question', 'favorited_by')


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'game', 'category')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')

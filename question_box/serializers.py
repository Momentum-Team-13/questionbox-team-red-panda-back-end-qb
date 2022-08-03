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


class CreateAnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    favorited_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")
    question = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'user', 'description', 'question', 'favorited_by')


class ViewAnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    favorited_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")
    question = serializers.SlugRelatedField(slug_field="title", read_only=True)
    question_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Answer
        fields = ('id', 'user', 'description', 'question', 'question_id', 'favorited_by')


class GameSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Game
        fields = ('id', 'game', 'category', 'category_id')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'favorited_by')

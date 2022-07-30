from rest_framework import serializers
from question_box.models import Question, User, Answer


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    favorited_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")

    class Meta:
        model = Question
        fields = ('pk', 'user', 'title', 'description', 'favorited_by')


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
from rest_framework import serializers
from question_box.models import Question, User


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    favorited_by = serializers.SlugRelatedField(queryset=User.objects.all(), many=True, slug_field="username")

    class Meta:
        model = Question
        fields = ('id', 'user', 'title', 'description', 'favorited_by')

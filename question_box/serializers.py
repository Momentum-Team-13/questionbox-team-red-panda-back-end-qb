from rest_framework import serializers
from question_box.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', '__all__')

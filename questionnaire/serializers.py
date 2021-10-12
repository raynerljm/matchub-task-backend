# serializers.py
from rest_framework import serializers

from .models import Question
from .models import Choice
from .models import Answer

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('questionId', 'question', 'questionType')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('choiceId', 'questionId', 'choice', 'label')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name', 'questionId', 'choiceId')
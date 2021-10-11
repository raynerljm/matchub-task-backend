from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .serializers import ChoiceSerializer
from .serializers import AnswerSerializer
from .models import Question
from .models import Choice
from .models import Answer

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('questionId')
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all().order_by('choiceId')
    serializer_class = ChoiceSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('name')
    serializer_class = AnswerSerializer

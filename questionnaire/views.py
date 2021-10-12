from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
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

    # def update(self, request, *args, **kwargs):
    #     choice_object = self.get_object()
    #     data = request.data

    #     choice_object.choiceId = data["choiceId"]
    #     choice_object.questionId = data["questionId"]
    #     choice_object.choice = data["choice"]
    #     choice_object.label = data["label"]

    #     choice_object.save()

    #     serializer = ChoiceSerializer(choice_object)

    #     return Response(serializer.data)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('name')
    serializer_class = AnswerSerializer

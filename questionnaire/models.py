from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Question(models.Model):
   questionId = models.IntegerField(primary_key=True)
   question = models.TextField()
   questionType = models.CharField(max_length=255)

   def __str__(self):
       return str(self.questionId) + ": "  + self.question + "(" + self.questionType + ")"

class Choice(models.Model):
   choiceId = models.IntegerField(primary_key=True)
   questionId = models.IntegerField()
   choice = models.CharField(max_length=255)
   label = models.CharField(max_length=255)

   def __str__(self):
       return "Question: " + str(self.questionId) + "; "  + str(self.choiceId) + ": " + self.label + "(" + self.choice + ")"

class Answer(models.Model):
    name = models.CharField(max_length=255)
    questionId = models.IntegerField()
    choiceId = models.IntegerField()
    # questionId = models.ForeignKey(Question, on_delete=CASCADE, to_field="questionId")
    # choiceId = models.ForeignKey(Choice, on_delete=CASCADE, to_field="choiceId")

    class Meta:
        unique_together = (("name", "questionId", "choiceId"))

    def __str__(self):
        return "Name:" + self.name + "; Question ID:" + str(self.questionId) + "; Choice ID: " + str(self.choiceId)




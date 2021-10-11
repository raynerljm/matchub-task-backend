from django.contrib import admin
from .models import Choice
from .models import Question
from .models import Answer

# Register your models here.
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Answer)

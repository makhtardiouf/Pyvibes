from django.contrib import admin
from .models import Question, Choice

# Register your models here, to enable CRUD with the admin UI

admin.site.register(Question)
admin.site.register(Choice)

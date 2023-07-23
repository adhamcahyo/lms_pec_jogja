from django.contrib import admin
from .models import Quiz, Question, Choice

class QuestionInline(admin.TabularInline):
    model = Question

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)

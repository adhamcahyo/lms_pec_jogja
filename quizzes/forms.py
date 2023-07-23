from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['content', 'is_correct']

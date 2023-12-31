from django import forms
from .models import Classroom

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['title', 'description', 'start_date', 'end_date']

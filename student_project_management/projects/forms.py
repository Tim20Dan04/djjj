# projects/forms.py

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'students', 'supervisor', 'technologies']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
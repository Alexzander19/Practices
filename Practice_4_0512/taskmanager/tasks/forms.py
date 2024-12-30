from django import forms
from .models import Project

class ProjectAddForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'description']
    labels = {'name': 'Название проекта: ',
              'description': 'Основные цели, описание'
            }
 
 

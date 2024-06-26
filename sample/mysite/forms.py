# myapp/forms.py

from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'actor', 'actoress']

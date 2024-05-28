from django import forms

class MovieForm(forms.Form):
    movie = forms.CharField(
        max_length=45, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control w-25', 'placeholder': 'Movie Name'})
    )
    year = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control w-25'})
    )
    actor = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control w-25', 'placeholder': 'Actor Name'})
    )
    actress = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control w-25', 'placeholder': 'Actress Name'})
    )

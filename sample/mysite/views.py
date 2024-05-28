from django.shortcuts import render
from .models import Movie


def initial(request):
    movies = Movie.objects.all()
    return render(request,"main.html",{"movies":movies})
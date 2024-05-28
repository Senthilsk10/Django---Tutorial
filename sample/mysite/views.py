from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm

def initial(request):
    movies = Movie.objects.all()
    return render(request,"main.html",{"movies":movies})


def formview(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.cleaned_data['movie']
            actor = form.cleaned_data['actor']
            actress = form.cleaned_data['actress']
            date = form.cleaned_data['year']
            
            Movie.objects.create(name=movie,actor=actor,actoress=actress,year=date)
        return redirect('index')
    
    form = MovieForm()
    return render(request,'form.html',{"form":form})
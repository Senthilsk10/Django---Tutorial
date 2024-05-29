from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,profile
from .forms import MovieForm
from .serializer import MovieSerializer
from rest_framework import generics


def movie_list(request):
    prof = profile.objects.get(id = request.user.id)
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies,'prof':prof})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie_detail.html', {'movie': movie})

def movie_create(request): 
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {'form': form})

def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movie_confirm_delete.html', {'movie': movie})



class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

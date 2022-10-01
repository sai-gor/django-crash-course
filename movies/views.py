from django.http import HttpResponse
from django.shortcuts import render

data = {
  'movies': [
    {
      'id': 1,
      'title': 'Jaws',
      'year': 1975
    },
    {
      'id': 2,
      'title': 'Training Day',
      'year': 2001
    },
    {
      'id': 3,
      'title': 'Scream',
      'year': 1996
    }
  ]
}

def movies(request):
  return render(request, 'movies/movies.html', data)

def home(request):
  return HttpResponse("Home page")
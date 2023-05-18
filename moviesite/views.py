from asyncio.windows_events import NULL
from http.client import HTTPResponse
from webbrowser import get
from django.shortcuts import render
from moviesite.models import createanime, createmovies
# Create your views here.
def home(request):
    anime = createanime.objects.all()
    movie = createmovies.objects.all()
    data ={
        "movie":movie,
        "anime":anime
    }
    return render(request,"home.html",data)
def movie(request):
    some = createmovies.objects.all()
    data ={
        "some":some
    }
    return render(request,"movie.html",data)
def base(request):
    return render(request,"base2.html")
def movieitem(request,val):
    createval = createmovies.objects.get(name=val)

    return render(request,"movieitem.html",{'createval':createval})
def anime(request):
    some = createanime.objects.all()
    data ={
        "some":some
    }
    return render(request,"anime.html",data)
def animeitem(request,val):
    createval = createanime.objects.get(name=val)

    return render(request,"animeitem.html",{'createval':createval})
def search(request):
    val = request.GET.get('serch')
    valdic ={
        "movie":createmovies.objects.filter(name__icontains = val),
        "anime":createanime.objects.filter(name__icontains = val)
    }
    return render(request,"search.html",valdic)